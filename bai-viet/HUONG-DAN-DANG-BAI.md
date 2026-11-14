# Quy trình đăng bài Blog lequydai.com/bai-viet (dành cho tác vụ tự động)

Lịch bài: Google Sheet "LỊCH BLOG LEQUYDAI.COM – ĐẠI LÊ AI"
(id 1GW4JnY6FtmHDxb0XjG8fDnkFSLKCxUO_GuYpg2O1zLA, trang "BLOG LEQUYDAI.COM").
Cột: A NGÀY · B CHUYÊN MỤC · C TIÊU ĐỀ · D TỪ KHÓA SEO · E BÀI VIẾT · F LINK BÀI ĐÃ ĐĂNG · G TIẾN ĐỘ · H DUYỆT · I GHI CHÚ

## Mỗi ngày
1. Tìm dòng có NGÀY = hôm nay (giờ Việt Nam). Cột F đã có link thì dừng, không đăng lại.
2. Cột E trống thì tự viết bài theo TIÊU ĐỀ, CHUYÊN MỤC, TỪ KHÓA SEO; ghi bài vào cột E, cột G = "Đã viết".
3. Thêm 1 mục vào `bai.json` → mảng `bai` với các trường:
   - `slug`: không dấu, nối gạch, ngắn (5–8 từ)
   - `cd`: đúng 1 trong 5 chuyên mục: Công cụ AI miễn phí · Chatbot Zalo chăm khách · Làm video bằng AI · Vận hành bằng Agent · Vibe Coding
   - `phut`, `ngay` (dd/mm/yyyy), `iso` (yyyy-mm-dd)
   - `tieu_de`: viết thường như câu bình thường (không VIẾT HOA cả câu)
   - `bia`: 3 dòng cho ảnh bìa, cách nhau bằng `|`, mỗi dòng ≤ 22 ký tự, dòng 2 được tô vàng
   - `anh`: luân phiên `dai-cuoi.jpg` / `dai-cuoi-3.jpg`
   - `mo_ta`: 1–2 câu (≤ 160 ký tự), có từ khoá SEO
   - `tra_loi`: ô "Trả lời nhanh" 2–3 câu, trả lời thẳng câu hỏi của tiêu đề
   - `than`: HTML, các mục `<h2>`, đoạn `<p>` ngắn, danh sách `<ul>/<ol>`, có ví dụ cụ thể
   - `o`: 2 ô giới thiệu cuối bài, chọn trong: congcu, donmay, chu, zaloai, vanhanh, video, vibe (hợp với chuyên mục)
4. Chạy `python3 bai-viet/_tao.py` rồi `python3 bai-viet/_bia.py` (tự tạo ảnh bìa cho bài mới).
5. Commit + push lên nhánh main của repo lequydailb-dotcom/lequydai-home. Trang lên mạng sau 1–2 phút.
6. Ghi vào Sheet: cột F = https://lequydai.com/bai-viet/<slug>/ · cột G = "Đã đăng".

## Luật viết
- Tiếng Việt thuần, giọng người thật, xưng "tôi" hoặc "Đại"; không dấu hiệu AI, không chen chữ tiếng Anh khi có từ Việt.
- Dễ làm, tự động, tiết kiệm thời gian; ví dụ cụ thể cho người bán hàng nhỏ.
- Luôn ghi "ChatGPT hoặc Claude", không chỉ một cái.
- Không bịa số liệu, không hứa doanh thu. Không có số thật thì nói chung chung.
- Mỗi đoạn dưới 150 chữ, cả bài dưới 600 chữ.
- Tên thương hiệu chỉ viết "ĐẠI LÊ AI".
- Trên web không có ô bình luận: kêu gọi nhắn Zalo 0972 782 782 hoặc vào nhóm Zalo, không ghi "bình luận bên dưới".
- Bài phải hợp chuyên mục và dẫn khéo về công cụ hoặc khoá học liên quan qua 2 ô cuối bài.
