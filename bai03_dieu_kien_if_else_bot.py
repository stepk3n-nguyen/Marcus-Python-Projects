"""
BÀI 03: ĐIỀU KIỆN RẼ NHÁNH (IF - ELIF - ELSE) & CHATBOT QUY TẮC V1.0
Dành cho học sinh lớp 7

Mục tiêu:
- Nắm vững tư duy logic rẽ nhánh: "NẾU (if) ... NẾU KHÔNG THÌ NẾU (elif) ... NGƯỢC LẠI (else)"
- Sử dụng các toán tử so sánh (==, !=, >, <) và từ khóa tìm kiếm chuỗi ('in')
- Xây dựng Chatbot trả lời theo kịch bản quy tắc cố định (Rule-based Bot)
"""

print("=== CHATBOT QUY TẮC CƠ BẢN V1.0 ===")
print("Xin chào! Hãy hỏi tôi một câu bất kỳ nhé.")

# Nhận tin nhắn từ người dùng
cau_hoi = input("Bạn: ")

# Chuẩn hóa tin nhắn: chuyển hết về chữ thường và xóa khoảng trắng thừa ở đầu/cuối
cau_hoi_chuan_hoa = cau_hoi.lower().strip()

# ----------------------------------------------------
# LOGIC TRẢ LỜI QUY TẮC (RULE-BASED LOGIC)
# ----------------------------------------------------
if "chào" in cau_hoi_chuan_hoa or "hello" in cau_hoi_chuan_hoa or "hi" in cau_hoi_chuan_hoa:
    print("Bot: Xin chào bạn! Chúc bạn một ngày học tập thật hiệu quả!")

elif "tên gì" in cau_hoi_chuan_hoa or "bạn là ai" in cau_hoi_chuan_hoa:
    print("Bot: Mình là Trợ Lý Lớp 7 được bạn lập trình bằng Python đấy!")

elif "mấy giờ" in cau_hoi_chuan_hoa or "thời gian" in cau_hoi_chuan_hoa:
    import datetime
    gio_hien_tai = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"Bot: Bây giờ là {gio_hien_tai} rồi nhé.")

elif "thời tiết" in cau_hoi_chuan_hoa:
    print("Bot: Hôm nay trời rất đẹp, thích hợp để ngồi học code Python cùng AI!")

elif "tạm biệt" in cau_hoi_chuan_hoa or "bye" in cau_hoi_chuan_hoa:
    print("Bot: Tạm biệt bạn! Hẹn gặp lại trong bài học tiếp theo nhé.")

else:
    # Đây là trường hợp bot "chưa được dạy" câu trả lời
    print("Bot: Xin lỗi, câu hỏi này mình chưa được lập trình câu trả lời.")

# ----------------------------------------------------
# 📝 BÀI TẬP THỰC HÀNH TẠI NHÀ CHO HỌC SINH:
# 1. Thêm ít nhất 3 câu hỏi mới vào bot:
#    - "bạn thích ăn gì?"
#    - "thủ đô của việt nam là gì?"
#    - "hôm nay là thứ mấy?" (Gợi ý: Dùng thư viện datetime)
# 2. Xử lý trường hợp người dùng gõ câu trống (không nhập gì mà ấn Enter).
# ----------------------------------------------------
