"""
BÀI 07: KHÁM PHÁ TRÍ TUỆ NHÂN TẠO (AI) & CƠ CHẾ HOẠT ĐỘNG CỦA API
Dành cho học sinh lớp 7

Mục tiêu:
- Hiểu sự khác biệt: Lập trình quy tắc (Rule-based) vs Trí tuệ nhân tạo (AI/LLM)
- Hiểu khái niệm API (Application Programming Interface) - "Cây cầu nối" giữa Code Python và Siêu máy tính AI
- Hiểu API Key là gì và cách bảo mật chìa khóa API
- Cài đặt thư viện kết nối mạng trong Python: `requests` hoặc thư viện AI
"""

# ====================================================
# 1. SO SÁNH: RULE-BASED VS AI (LLM)
# ====================================================
"""
+-------------------------+--------------------------------------------------------+
| LẬP TRÌNH QUY TẮC       | TRÍ TUỆ NHÂN TẠO (AI / LLM như ChatGPT, Gemini)        |
| (Rule-based với if/else)|                                                        |
+-------------------------+--------------------------------------------------------+
| - Con người phải tự viết| - Mô hình AI đã đọc hàng triệu cuốn sách trên Internet.|
|   từng câu if/elif.     | - Tự động hiểu ngữ cảnh và ngôn ngữ tự nhiên của người |
| - Gõ sai 1 chữ là bot   |   dùng, dù gõ tắt hay sai chính tả vẫn hiểu được.      |
|   không hiểu được.      | - Trả lời được kiến thức ở mọi môn học: Toán, Văn,     |
| - Ưu điểm: Nhanh, bảo mật|   Lịch sử, Khoa học, Dịch thuật...                     |
|   và hoàn toàn miễn phí.| - Nhược điểm: Cần kết nối Internet & có API Key.       |
+-------------------------+--------------------------------------------------------+
"""

# ====================================================
# 2. API LÀ GÌ? HÃY TƯỞNG TƯỢNG NHƯ ĐI NHÀ HÀNG:
# ====================================================
"""
- BẠN (Chương trình Python của học sinh)  ---> Khách hàng gọi món
- NGƯỜI BỒI BÀN (API)                     ---> Nhận yêu cầu và chuyển vào bếp
- NHÀ BẾP / ĐẦU BẾP (Máy chủ OpenAI/Google) -> Nấu món (Xử lý câu trả lời bằng AI)
- BỒI BÀN (API)                           ---> Bưng đĩa thức ăn trả về cho Bạn
"""

# ====================================================
# 3. HƯỚNG DẪN CÀI ĐẶT THƯ VIỆN CẦN THIẾT
# ====================================================
print("=== HƯỚNG DẪN CÀI ĐẶT MÔI TRƯỜNG CHO BÀI HỌC AI ===")
print("Thầy cô/Học sinh mở Terminal (Command Prompt) và chạy các lệnh sau:\n")
print("   pip install requests")
print("   pip install google-genai      (Dành cho Google Gemini AI)")
print("   pip install openai            (Dành cho ChatGPT OpenAI)")
print("   pip install gTTS pygame       (Dành cho giọng nói AI ở Bài 10)")
print("   pip install customtkinter     (Dành cho giao diện đẹp ở Bài 11)")
print("\n" + "=" * 55)

# ====================================================
# 4. VÍ DỤ MÔ PHỎNG: GỬI DỮ LIỆU ĐẾN API
# ====================================================
import json

# Một gói tin (Payload) chuẩn bị gửi lên AI trông sẽ như thế này:
goi_tin_mau = {
    "model": "gemini-2.5-flash / gpt-4o-mini",
    "messages": [
        {"role": "system", "content": "Bạn là một gia sư AI thân thiện dạy học sinh lớp 7."},
        {"role": "user", "content": "Tại sao lá cây lại có màu xanh?"}
    ],
    "temperature": 0.7  # Độ sáng tạo của AI (từ 0.0 đến 1.0)
}

print("Dữ liệu định dạng JSON chuẩn bị truyền qua API:")
print(json.dumps(goi_tin_mau, indent=4, ensure_ascii=False))

# ----------------------------------------------------
# 📝 HƯỚNG DẪN LẤY API KEY MIỄN PHÍ DÀNH CHO LỚP HỌC:
# 1. Google Gemini API (Miễn phí 100%):
#    - Truy cập: https://aistudio.google.com/
#    - Đăng nhập tài khoản Google -> Bấm 'Create API key' -> Copy mã Key.
# 2. Lưu API Key vào 1 biến bảo mật trong file code ở Bài 08!
# ----------------------------------------------------
