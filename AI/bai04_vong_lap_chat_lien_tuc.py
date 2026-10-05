"""
BÀI 04: VÒNG LẶP (WHILE, FOR) & GIỮ CHO CHATBOT CHẠY LIÊN TỤC
Dành cho học sinh lớp 7

Mục tiêu:
- Hiểu cách hoạt động của vòng lặp `while True` (vòng lặp vô tận)
- Biết cách dùng lệnh `break` để thoát khỏi vòng lặp khi gặp điều kiện dừng
- Biết dùng lệnh `continue` để bỏ qua lượt lặp hiện tại
- Nâng cấp Chatbot trò chuyện liên tục mà không bị tắt chương trình
"""

import datetime

print("====================================================")
print("CHATBOT THÔNG MINH PHIÊN BẢN CHẠY LIÊN TỤC")
print("(Gõ 'tam biet', 'thoat' hoặc 'exit' để dừng cuộc trò chuyện)")
print("====================================================\n")

# Vòng lặp while True giúp chương trình không bị kết thúc sau 1 câu trả lời
while True:
    cau_hoi = input("\nBạn: ")
    cau_hoi_chuan_hoa = cau_hoi.lower().strip()

    # 1. Kiểm tra nếu người dùng không nhập gì
    if not cau_hoi_chuan_hoa:
        print("Bot: Ơ, bạn chưa gõ gì kìa! Hãy hỏi mình điều gì đó đi.")
        continue

    # 2. Điều kiện thoát chương trình (break)
    if cau_hoi_chuan_hoa in ["tam biet", "tạm biệt", "bye", "exit", "thoat", "thoát"]:
        print("Bot: Tạm biệt bạn nhé! Chúc bạn học giỏi và có một ngày tuyệt vời!")
        break

    # 3. Kịch bản trả lời tự động
    if "chao" in cau_hoi_chuan_hoa or "chào" in cau_hoi_chuan_hoa or "hi" in cau_hoi_chuan_hoa:
        print("Bot: Chào bạn! Mình có thể giúp gì cho bạn hôm nay?")

    elif "gio" in cau_hoi_chuan_hoa or "giờ" in cau_hoi_chuan_hoa:
        bay_gio = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Bot: Hiện tại là {bay_gio}.")

    elif "ngay" in cau_hoi_chuan_hoa or "ngày" in cau_hoi_chuan_hoa:
        hom_nay = datetime.datetime.now().strftime("%d/%m/%Y")
        print(f"Bot: Hôm nay là ngày {hom_nay}.")

    elif "toan" in cau_hoi_chuan_hoa or "tính" in cau_hoi_chuan_hoa:
        print("Bot: Bạn muốn tính toán gì? Hãy gõ biểu thức (ví dụ: 15 + 25):")
        phep_tinh = input("   Phép tính: ")
        try:
            # eval() giúp tính toán trực tiếp chuỗi biểu thức số học
            ket_qua = eval(phep_tinh)
            print(f"Bot: Kết quả là: {ket_qua}")
        except Exception:
            print("Bot: Phép tính không hợp lệ rồi bạn ơi!")

    elif "ai tao ra ban" in cau_hoi_chuan_hoa or "ai tạo ra bạn" in cau_hoi_chuan_hoa:
        print("Bot: Mình được một lập trình viên nhí lớp 7 tài năng tạo ra đấy! 🎉🎉🎉")

    else:
        print("Bot: Câu này mình chưa học trong bộ nhớ. Thử hỏi câu khác xem sao nhé!")

# ----------------------------------------------------
# 📝 BÀI TẬP THỰC HÀNH TẠI NHÀ CHO HỌC SINH:
# 1. Thêm tính năng đếm số lượng câu hỏi mà người dùng đã hỏi trong suốt phiên trò chuyện.
#    (Gợi ý: Khởi tạo biến dem_cau_hoi = 0 ngoài vòng lặp, mỗi lần hỏi tăng 1).
# 2. Khi người dùng thoát (break), in ra tổng số câu hỏi đã trò chuyện.
# ----------------------------------------------------
