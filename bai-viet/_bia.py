# Tạo ảnh bìa 1200x630 cho bài Blog: python3 bai-viet/_bia.py [slug ...]
# Không có slug thì tạo cho bài nào chưa có ảnh. Cần: pip install playwright && playwright install chromium
import json, os, sys, asyncio
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(D)
data = json.load(open(f'{D}/bai.json', encoding='utf-8'))
ds = data['bai'] + data['khoa_hoc']
chon = sys.argv[1:]

# Tự chọn ảnh cho bài chưa có "anh": lấy ảnh trong img/blog dùng ít nhất, tránh ảnh vừa dùng gần đây
import glob
POOL = sorted(os.path.relpath(f, f'{R}/img') for f in glob.glob(f'{R}/img/blog/*.jpg'))
def _chon_anh():
    gan = [b.get('anh') for b in sorted(data['bai'], key=lambda b: b['iso'], reverse=True) if b.get('anh')]
    dem = {a: gan.count(a) for a in POOL}
    vitri = {a: (gan.index(a) if a in gan else 10**6) for a in POOL}
    return sorted(POOL, key=lambda a: (dem[a], -vitri[a]))[0]
_doi = False
for b in data['bai'] + data['khoa_hoc']:
    if not b.get('anh') and POOL:
        b['anh'] = _chon_anh(); _doi = True
if _doi:
    json.dump(data, open(f'{D}/bai.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
ds = [b for b in ds if b['slug'] in chon] if chon else [b for b in ds if not os.path.exists(f"{D}/anh/{b['slug']}.jpg")]
T = '''<html><head><style>
@font-face{font-family:L;src:url(file://%(D)s/_font/Lora-Variable.ttf)}
@font-face{font-family:I;font-weight:600;src:url(file://%(D)s/_font/Inter-SemiBold.otf)}
@font-face{font-family:I;font-weight:700;src:url(file://%(D)s/_font/Inter-Bold.otf)}
body{margin:0;width:1200px;height:630px;background:#F5F1E6;font-family:I;position:relative;overflow:hidden}
.logo{position:absolute;left:64px;top:52px;height:44px}
.tag{position:absolute;left:64px;top:150px;font:700 20px I;letter-spacing:.08em;text-transform:uppercase;color:#FD7800}
h1{position:absolute;left:60px;top:190px;width:680px;margin:0;font:600 64px/1.18 L;color:#041431}
.v{background:linear-gradient(transparent 60%%,#FED227 60%%,#FED227 92%%,transparent 92%%)}
.web{position:absolute;left:64px;bottom:48px;font:600 20px I;color:#5A6478}
.anh{position:absolute;right:56px;top:48px;width:360px;height:534px;border-radius:22px;overflow:hidden;border:1px solid #E2DCCB}
.anh img{width:100%%;height:100%%;object-fit:cover;object-position:50%% 25%%}
.vach{position:absolute;right:0;top:0;bottom:0;width:470px;background:#ECE6D6}
</style></head><body><div class="vach"></div>
<img class="logo" src="file://%(R)s/img/logo-duong.png">
<div class="tag">%(cd)s</div><h1>%(t)s</h1><div class="web">lequydai.com/bai-viet</div>
<div class="anh"><img src="file://%(R)s/img/%(anh)s"></div></body></html>'''
async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1200, 'height': 630})
        for x in ds:
            l = (x['bia'].split('|') + ['', '', ''])[:3]
            h = T % dict(D=D, R=R, cd=x['cd'], anh=x.get('anh', 'dai-cuoi.jpg'), t=f"{l[0]}<br><span class='v'>{l[1]}</span><br>{l[2]}")
            open('/tmp/_bia.html', 'w').write(h); await pg.goto('file:///tmp/_bia.html'); await pg.wait_for_timeout(400)
            await pg.screenshot(path=f"{D}/anh/{x['slug']}.jpg", type='jpeg', quality=86); print('bìa', x['slug'])
        await b.close()
asyncio.run(main())
