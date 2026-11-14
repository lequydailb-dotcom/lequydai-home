# Tạo trang Blog ĐẠI LÊ AI: python3 bai-viet/_tao.py  (chạy ở thư mục gốc repo)
import json, os, html
D = os.path.dirname(os.path.abspath(__file__))
FONT = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,500;8..60,600&display=swap" rel="stylesheet"><link rel="stylesheet" href="/css/moi.css?v=1">'
ZALO = 'https://zalo.me/g/a9my3sx1ov0fsihenx6e'

DAU = '''<header class="dau"><div class="khung">
<a href="/"><img src="/img/logo-duong.png" alt="ĐẠI LÊ AI"></a>
<button class="mo-menu" aria-label="Mở menu" onclick="document.querySelector('.menu').classList.toggle('mo')">☰</button>
<nav class="menu"><a href="/#san-pham">Sản phẩm</a><a href="/#khoa-hoc">Khoá học</a><a href="https://congcu.lequydai.com">Công cụ miễn phí</a><a href="/bai-viet/">Blog</a><a href="https://hoc.lequydai.com">Học viên</a><a class="nut nut-nho" href="%s">Nhóm Zalo miễn phí</a></nav>
</div></header>''' % ZALO
CHAN = '''<footer class="chan"><div class="khung"><img src="/img/logo-duong.png" alt="ĐẠI LÊ AI">
<a href="/#san-pham">Sản phẩm</a><a href="/#khoa-hoc">Khoá học</a><a href="https://congcu.lequydai.com">Công cụ</a><a href="/bai-viet/">Blog</a><a href="https://hoc.lequydai.com">Học viên</a><a href="https://zalo.me/0972782782">Zalo 0972 782 782</a><a href="/dieu-khoan/">Điều khoản</a><a href="/chinh-sach-bao-mat/">Chính sách bảo mật</a>
<span style="width:100%%">© 2026 lequydai.com</span></div></footer>
<div class="thanh"><span>Công cụ miễn phí, hỏi đáp trực tiếp</span><a class="nut nut-nho" href="%s">Nhóm Zalo</a></div>''' % ZALO

CHU_DE = ['Công cụ AI miễn phí', 'Chatbot Zalo chăm khách', 'Làm video bằng AI', 'Vận hành bằng Agent', 'Vibe Coding']

O = {
 'donmay': ('sang', 'Nhận DỌN MÁY miễn phí', 'File nằm trong tin nhắn đã ghim của nhóm Zalo. Vào nhóm, tải về, 2 nút bấm là xong.', 'Vào nhóm Zalo nhận file →', ZALO),
 'congcu': ('sang', 'Dùng thử 4 công cụ AI miễn phí của ĐẠI LÊ AI', 'Nói ra chữ, Tóm ảnh, Dọn máy, Cắt nhanh: bấm là có kết quả, không cần mua.', 'Xem 4 công cụ miễn phí →', 'https://congcu.lequydai.com/#mien-phi'),
 'chu': ('sang', 'Dùng thử NÓI RA CHỮ ngay', 'Chạy trên trình duyệt, miễn phí, chỉ cần khoá Gemini của bạn.', 'Mở chu.lequydai.com →', 'https://chu.lequydai.com'),
 'zaloai': ('', 'Zalo AI: bot soạn tin trả lời khách cho bạn', 'Bắt đầu bằng chế độ Nháp, bạn duyệt rồi bot mới gửi. Gói 1 năm 990.000đ, gói trọn đời 1.990.000đ cho 1 máy.', 'Xem Zalo AI →', 'https://congcu.lequydai.com/zalo-ai/'),
 'vanhanh': ('', 'Muốn việc lặp lại tự chạy mỗi ngày?', 'Khoá VẬN HÀNH AGENT chỉ bạn dựng đội nhân viên AI: giao việc, hẹn giờ cho AI tự làm, chatbot trả lời khách. Cầm tay chỉ việc, 16 bài.', 'Xem khoá VẬN HÀNH AGENT →', '/van-hanh/'),
 'video': ('', 'Có chữ rồi, làm luôn thành video', 'Khoá tặng miễn phí: làm video AI đầu tiên trong 30 phút, có giọng nói, không cần lên hình.', 'Nhận khoá tặng →', 'https://hoc.lequydai.com/tang/dang-ky/'),
 'vibe': ('', 'Muốn tự làm chatbot của riêng bạn?', 'Khoá 28 NGÀY VIBE CODING: tự làm bot chăm khách trên Zalo và Facebook bằng AI, mỗi ngày một bước nhỏ.', 'Xem khoá 28 NGÀY VIBE CODING →', '/vibe-coding/'),
}

_D = json.load(open(os.path.join(D, 'bai.json'), encoding='utf-8'))
BAI = _D['bai']
KH = _D['khoa_hoc']
BAI.sort(key=lambda b: b['iso'], reverse=True)  # bài mới nhất lên đầu

def o_html(k):
    kieu, h, p, nut, url = O[k]
    return f'<aside class="o-qua {kieu}"><h2>{h}</h2><p>{p}</p><a class="nut" href="{url}">{nut}</a></aside>'

def trang(b):
    lien = [x for x in BAI if x['slug'] != b['slug']][:2]
    ld = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": b['tieu_de'], "description": b['mo_ta'], "datePublished": b['iso'], "author": {"@type": "Person", "name": "Lê Quý Đại"}, "image": f"https://lequydai.com/bai-viet/anh/{b['slug']}.jpg", "publisher": {"@type": "Organization", "name": "ĐẠI LÊ AI"}}
    the = ''.join(f'<a class="the-bai" href="/bai-viet/{x["slug"]}/"><img src="/bai-viet/anh/{x["slug"]}.jpg" alt="" loading="lazy"><div class="nd"><span class="nhan">{x["cd"]}</span><h3>{x["tieu_de"]}</h3></div></a>' for x in lien)
    return f'''<!DOCTYPE html>
<html lang="vi"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(b['tieu_de'])} – ĐẠI LÊ AI</title>
<meta name="description" content="{html.escape(b['mo_ta'])}">
<meta property="og:title" content="{html.escape(b['tieu_de'])}"><meta property="og:description" content="{html.escape(b['mo_ta'])}">
<meta property="og:image" content="https://lequydai.com/bai-viet/anh/{b['slug']}.jpg"><meta property="og:type" content="article">
<link rel="icon" href="/img/cover-square.jpg?v=20261105">{FONT}
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script></head>
<body>{DAU}
<main><article class="bai">
<a class="nho" href="/bai-viet/" style="text-decoration:none">← Blog</a>
<div class="meta"><span class="cd">{b['cd']}</span><span>{b['phut']} phút đọc</span><span>Ngày {b['ngay']}</span></div>
<h1>{b['tieu_de']}</h1>
<p class="phu">{b['mo_ta']}</p>
<div class="bia"><img src="/bai-viet/anh/{b['slug']}.jpg" alt="{html.escape(b['tieu_de'])}"></div>
<div class="tra-loi"><b>Trả lời nhanh</b><p>{b['tra_loi']}</p></div>
{b['than']}
{''.join(o_html(k) for k in b['o'])}
</article>
<section class="lien-quan"><h2>Bài liên quan</h2><div class="luoi luoi-2">{the}</div></section>
</main>{CHAN}</body></html>'''

for b in BAI:
    os.makedirs(f'{D}/{b["slug"]}', exist_ok=True)
    open(f'{D}/{b["slug"]}/index.html', 'w').write(trang(b))

ds = [{k: b[k] for k in ('slug', 'cd', 'tieu_de', 'mo_ta', 'ngay')} for b in BAI] + [{'slug': k['slug'], 'cd': k['cd'], 'tieu_de': k['tieu_de'], 'mo_ta': k['mo_ta'], 'url': k['url'], 'loai': 'Khoá học'} for k in KH]
open(f'{D}/ds.js', 'w').write('window.BAI_VIET=' + json.dumps(ds, ensure_ascii=False) + ';')
json.dump([{k: b[k] for k in ('slug', 'bia', 'anh', 'cd')} for b in BAI + KH], open('/tmp/bia.json', 'w'), ensure_ascii=False)

loc = ''.join(f'<button data-cd="{c}">{c}</button>' for c in CHU_DE)
open(f'{D}/index.html', 'w').write(f'''<!DOCTYPE html>
<html lang="vi"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Blog – ĐẠI LÊ AI</title>
<meta name="description" content="Bài viết dễ làm về AI cho người kinh doanh: công cụ miễn phí, chatbot Zalo, làm video bằng AI, vận hành bằng Agent, Vibe Coding.">
<link rel="icon" href="/img/cover-square.jpg?v=20261105">{FONT}</head>
<body>{DAU}
<main class="khoi"><div class="khung">
<div class="dau-khoi"><span class="nhan">Blog</span><h1>AI cho người kinh doanh, <span class="vet">nói bằng lời thường</span>.</h1>
<p class="phu">Mỗi bài giải quyết một việc cụ thể: dễ làm, làm được ngay, tiết kiệm thời gian.</p></div>
<div class="loc"><button class="on" data-cd="">Tất cả</button>{loc}</div>
<div class="luoi luoi-3" id="ds"></div>
</div></main>{CHAN}
<script src="/bai-viet/ds.js?v=2"></script>
<script>
function ve(cd){{document.getElementById('ds').innerHTML=BAI_VIET.filter(function(b){{return !cd||b.cd===cd}}).map(function(b){{return '<a class="the-bai" href="'+(b.url||'/bai-viet/'+b.slug+'/')+'"><img src="/bai-viet/anh/'+b.slug+'.jpg" alt="" loading="lazy"><div class="nd"><span class="nhan">'+(b.loai?'Khoá học · ':'')+b.cd+'</span><h3>'+b.tieu_de+'</h3><p>'+b.mo_ta+'</p></div></a>'}}).join('')||'<p class="phu">Chủ đề này sắp có bài, bạn quay lại sau nhé.</p>'}}
document.querySelectorAll('.loc button').forEach(function(x){{x.onclick=function(){{document.querySelectorAll('.loc button').forEach(function(y){{y.classList.remove('on')}});x.classList.add('on');ve(x.dataset.cd)}}}});ve('');
</script></body></html>''')
print('ok', len(BAI))
