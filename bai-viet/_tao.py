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
 'chu': ('sang', 'Dùng thử NÓI RA CHỮ ngay', 'Chạy trên trình duyệt, miễn phí, chỉ cần khoá Gemini của bạn.', 'Mở chu.lequydai.com →', 'https://chu.lequydai.com'),
 'zaloai': ('', 'Zalo AI: bot soạn tin trả lời khách cho bạn', 'Bắt đầu bằng chế độ Nháp, bạn duyệt rồi bot mới gửi. Gói 1 năm 990.000đ, gói trọn đời 1.990.000đ cho 1 máy.', 'Xem Zalo AI →', 'https://congcu.lequydai.com/zalo-ai/'),
 'vanhanh': ('', 'Muốn việc lặp lại tự chạy mỗi ngày?', 'Khoá VẬN HÀNH AGENT chỉ bạn dựng đội nhân viên AI: giao việc, hẹn giờ cho AI tự làm, chatbot trả lời khách. Cầm tay chỉ việc, 16 bài.', 'Xem khoá VẬN HÀNH AGENT →', '/van-hanh/'),
 'video': ('', 'Có chữ rồi, làm luôn thành video', 'Khoá tặng miễn phí: làm video AI đầu tiên trong 30 phút, có giọng nói, không cần lên hình.', 'Nhận khoá tặng →', 'https://hoc.lequydai.com/tang/dang-ky/'),
 'vibe': ('', 'Muốn tự làm chatbot của riêng bạn?', 'Khoá 28 NGÀY VIBE CODING: tự làm bot chăm khách trên Zalo và Facebook bằng AI, mỗi ngày một bước nhỏ.', 'Xem khoá 28 NGÀY VIBE CODING →', '/vibe-coding/'),
}

BAI = [
 dict(slug='may-cham-o-c-day', cd=CHU_DE[0], phut=3, ngay='13/11/2026', iso='2026-11-13',
  tieu_de='Máy chậm, ổ C đầy: dọn rác an toàn trong 2 nút bấm',
  bia='Máy chậm, ổ C đầy?|Dọn an toàn|trong 2 nút bấm', anh='dai-cuoi.jpg',
  mo_ta='Không biết xoá gì cho an toàn nên cứ để ổ C đỏ mãi. Cách dọn đúng chỗ rác, không đụng tới ảnh, video, tài liệu của bạn.',
  tra_loi='Rác làm đầy ổ C chủ yếu nằm ở 4 chỗ: tệp tạm của Windows, bộ nhớ đệm trình duyệt, bộ nhớ đệm phần mềm dựng video và thùng rác. Dọn đúng 4 chỗ này là an toàn. Công cụ DỌN MÁY miễn phí làm việc đó bằng 2 nút: QUÉT rồi DỌN NGAY.',
  than='''<p>Nhiều người thấy ổ C báo đỏ là hoảng, rồi xoá bừa vài thư mục lạ. Có người xoá nhầm cả dự án video đang làm dở. Thật ra rác nằm ở vài chỗ cố định, biết đúng chỗ thì dọn rất nhẹ nhàng.</p>
<h2>Rác nằm ở đâu</h2>
<ul><li><b>Tệp tạm (Temp)</b>: Windows và phần mềm tạo ra khi chạy, dùng xong là bỏ.</li>
<li><b>Bộ nhớ đệm trình duyệt</b>: Chrome, Edge, Cốc Cốc, Firefox lưu tạm hình ảnh trang web. Xoá đi, lần sau trang tự tải lại.</li>
<li><b>Bộ nhớ đệm CapCut, Premiere</b>: file xem trước khi dựng video. Không phải dự án của bạn.</li>
<li><b>Thùng rác</b>: file bạn đã xoá nhưng vẫn chiếm chỗ.</li></ul>
<h2>Dọn bằng DỌN MÁY trong 2 nút</h2>
<ol><li>Vào nhóm Zalo, mở tin nhắn đã ghim, tải file DonMay về.</li>
<li>Chuột phải vào file, chọn Extract All để giải nén.</li>
<li>Bấm đúp DonMay.bat, rồi bấm <b>1. QUÉT</b>. Máy hiện từng nhóm rác chiếm bao nhiêu chỗ.</li>
<li>Bấm <b>2. DỌN NGAY</b> là xong.</li></ol>
<p>Nếu Windows hiện "Windows protected your PC", bấm More info rồi Run anyway. Đây là cảnh báo bình thường với file tải về.</p>
<h2>Những thứ công cụ không đụng tới</h2>
<p>Ảnh, video, tài liệu, Desktop, Downloads, mật khẩu và tài khoản đăng nhập đều giữ nguyên. Riêng thùng rác sẽ được dọn sạch, nên cần lấy lại file nào thì lấy trước khi bấm DỌN.</p>
<h2>Bao lâu dọn một lần</h2>
<p>Mỗi tháng một lần là đủ. Nếu bạn dựng video nhiều, bộ nhớ đệm đầy nhanh hơn, có thể dọn mỗi tuần.</p>''',
  o=['donmay','vanhanh']),
 dict(slug='ghi-am-thanh-chu', cd=CHU_DE[0], phut=3, ngay='13/11/2026', iso='2026-11-13',
  tieu_de='Họp Zoom xong khỏi gõ lại: biến file ghi âm thành chữ, kịch bản, bài đăng',
  bia='Họp Zoom xong|khỏi gõ lại|biên bản', anh='dai-cuoi-3.jpg',
  mo_ta='Một file ghi âm cho ra 4 thứ: văn bản chép lời, kịch bản thu âm, bài Facebook, biên bản họp. Làm trên trình duyệt, miễn phí.',
  tra_loi='Dùng công cụ NÓI RA CHỮ (chu.lequydai.com): dán khoá Gemini miễn phí, chọn file ghi âm hoặc video, tích kết quả muốn nhận rồi bấm Bắt đầu. Vài phút sau có đủ chữ để copy hoặc tải về.',
  than='''<p>Họp một tiếng, gõ lại biên bản mất thêm hai tiếng. Quay video nói chuyện xong, lại ngồi chép lời để viết bài. Đây là việc AI làm rất tốt, và bạn không cần cài gì cả.</p>
<h2>Bước 1: dán khoá Gemini</h2>
<p>Vào chu.lequydai.com, dán khoá Gemini rồi bấm Lưu khoá. Khoá này lấy miễn phí trong Google AI Studio, dán một lần là xong. Nên chọn mô hình gemini-2.5-flash, vừa nhanh vừa đủ tốt.</p>
<h2>Bước 2: đưa âm thanh vào</h2>
<p>Bấm chọn file ghi âm hoặc video. Công cụ nhận mp3, m4a, wav, mp4, webm, mkv. Không có file sẵn thì bấm Ghi âm ngay, nói thẳng vào máy. Đã có văn bản thì dán vào ô chữ.</p>
<h2>Bước 3: chọn thứ muốn nhận</h2>
<ul><li><b>Kịch bản thu âm</b> cho video ngắn.</li>
<li><b>Bài đăng Facebook</b> đăng được ngay.</li>
<li><b>Biên bản họp</b> cho buổi Zoom.</li>
<li><b>Tóm tắt ý chính</b> khi chỉ cần đọc nhanh.</li></ul>
<p>Văn bản chép lời luôn có. Chọn càng nhiều thì chờ càng lâu một chút.</p>
<h2>Mẹo để chữ ra chính xác hơn</h2>
<p>Ghi âm ở chỗ yên tĩnh, nói rõ, để điện thoại gần người nói. Chưa có file để thử thì bấm Dùng thử dữ liệu mẫu rồi bấm Bắt đầu, xem kết quả trước khi dùng thật.</p>''',
  o=['chu','video']),
 dict(slug='chatbot-zalo-can-gi', cd=CHU_DE[1], phut=3, ngay='13/11/2026', iso='2026-11-13',
  tieu_de='Chatbot trả lời khách trên Zalo: cần chuẩn bị những gì trước khi bật',
  bia='Chatbot Zalo|trả lời khách|cần chuẩn bị gì?', anh='dai-cuoi.jpg',
  mo_ta='Bot trả lời hay hay dở phụ thuộc vào thứ bạn nạp cho nó. 4 thứ cần chuẩn bị và cách bật bot mà không sợ trả lời sai.',
  tra_loi='Trước khi bật chatbot Zalo, chuẩn bị 4 thứ: bảng giá, chính sách (giao hàng, đổi trả), các câu khách hay hỏi kèm câu trả lời mẫu, và giọng nói chuyện của bạn. Rồi bắt đầu ở chế độ Nháp: bot soạn, bạn duyệt rồi mới gửi.',
  than='''<p>Khách nhắn Zalo cả ngày, trả lời chậm là mất khách. Chatbot giúp được, nhưng bot chỉ trả lời đúng khi bạn cho nó biết bạn bán gì, giá bao nhiêu, và nói chuyện thế nào.</p>
<h2>4 thứ cần chuẩn bị</h2>
<ol><li><b>Bảng giá</b>: sản phẩm, giá, quà tặng đang chạy.</li>
<li><b>Chính sách</b>: giao hàng, thanh toán, đổi trả, bảo hành.</li>
<li><b>Câu hỏi hay gặp</b>: 10 đến 20 câu khách hỏi nhiều nhất, kèm câu bạn vẫn trả lời.</li>
<li><b>Giọng của bạn</b>: xưng hô thế nào, gọi khách là gì, câu chào quen thuộc.</li></ol>
<p>Viết ra giấy hay file Word đều được. Bot đọc những thứ này để trả lời đúng giọng bạn.</p>
<h2>Bật bot thế nào cho yên tâm</h2>
<p>Zalo AI bắt đầu ở <b>chế độ Nháp</b>: bot đọc tin khách và soạn sẵn câu trả lời, bạn xem rồi bấm gửi. Có ô Thử bot để bạn gõ như khách mà không gửi lên Zalo. Khi đã tin bot trả lời đúng, bạn mới bật chế độ Tự động.</p>
<h2>Bot nhớ từng khách</h2>
<p>Bot nhớ 40 lượt chat gần nhất của mỗi khách, nên khách quay lại hỏi tiếp vẫn hiểu đang nói chuyện gì, không phải hỏi lại từ đầu.</p>
<h2>Cần gì để chạy</h2>
<p>Zalo AI chạy trên Zalo cá nhân, cài trên máy Windows có Zalo PC, nên máy cần bật lúc bot làm việc. Chưa rõ việc của mình có hợp không, nhắn Zalo 0972 782 782 hỏi Đại trước.</p>''',
  o=['zaloai','vibe']),
]

KH = [
 dict(slug='kh-van-hanh-agent', cd=CHU_DE[3], url='/van-hanh/', tieu_de='Khoá VẬN HÀNH AGENT: dựng trợ lý AI tự làm việc theo não của bạn',
  mo_ta='16 bài cầm tay chỉ việc: cài NAOSO, dựng đội nhân viên AI, hẹn giờ cho AI tự làm, chatbot khách hàng, chạy 24/7 với tên miền riêng.',
  bia='Khoá VẬN HÀNH AGENT|trợ lý AI tự làm|việc mỗi ngày', anh='dai-cuoi-3.jpg'),
 dict(slug='kh-28-ngay-vibe-coding', cd=CHU_DE[4], url='/vibe-coding/', tieu_de='Khoá 28 NGÀY VIBE CODING: tự làm bot chăm khách Zalo, Facebook bằng AI',
  mo_ta='28 ngày tự tay làm bot chăm sóc khách trả lời tự động trên Zalo và Facebook bằng AI, không cần biết code.',
  bia='28 ngày Vibe Coding|tự làm chatbot|không cần code', anh='dai-cuoi.jpg'),
 dict(slug='kh-lam-video-khong-len-hinh', cd=CHU_DE[2], url='https://hoc.lequydai.com/khong-len-hinh/dang-ky/', tieu_de='Khoá LÀM VIDEO KHÔNG CẦN LÊN HÌNH: thu âm giọng là có video mỗi ngày',
  mo_ta='Thu âm giọng, ghép hình quay sẵn, video Veo 3 và nguồn miễn phí thành video đăng mỗi ngày. 14 bài đi từng bước.',
  bia='Làm video|không cần lên hình|đăng mỗi ngày', anh='dai-cuoi-3.jpg'),
 dict(slug='kh-khoa-tang-video-ai', cd=CHU_DE[2], url='https://hoc.lequydai.com/tang/dang-ky/', tieu_de='Khoá tặng miễn phí: làm video AI đầu tiên trong 30 phút',
  mo_ta='10 bài ngắn làm video AI có tiếng nói với ChatGPT hoặc Gemini và Google Flow, kèm 50 câu lệnh cho 10 ngành. Miễn phí.',
  bia='Khoá tặng miễn phí|video AI đầu tiên|trong 30 phút', anh='dai-cuoi.jpg'),
]

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
