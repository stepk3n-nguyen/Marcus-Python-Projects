"""
BÀI 05: DANH SÁCH (LIST), TỪ ĐIỂN (DICTIONARY) & BOT CÓ BỘ NHỚ
Dành cho học sinh lớp 7

Mục tiêu:
- Sử dụng Danh sách (List) để lưu nhiều câu trả lời khác nhau và chọn ngẫu nhiên bằng `random.choice()`
- Sử dụng Từ điển (Dictionary `key: value`) để tạo cơ sở dữ liệu tra cứu nhanh
- Giúp Bot trả lời phong phú, tự nhiên, không bị lặp lại một câu nhàm chán
"""

import random

# ----------------------------------------------------
# 1. DANH SÁCH CÂU TRẢ LỜI NGẪU NHIÊN (LIST)
# ----------------------------------------------------
danh_sach_chao = [
    "Chào bạn nha! Rất vui được gặp bạn.",
    "Hello người bạn thông thái!",
    "Chào đằng ấy, hôm nay có gì vui không?",
    "Hi bạn! Tôi có thể hỗ trợ gì cho bạn nào?"
]

danh_sach_khen = [
    "Bạn thông minh thật đấy!",
    "Câu hỏi rất hay, bạn đúng là học sinh chăm chỉ!",
    "Quá đỉnh luôn bạn ơi! 🌟"
]

# ----------------------------------------------------
# 2. TỪ ĐIỂN TRI THỨC (DICTIONARY) DẠNG TỪ KHÓA -> CÂU TRẢ LỜI
# ----------------------------------------------------
tu_dien_thu_do = {
    "việt nam": "Hà Nội",
    "nhật bản": "Tokyo",
    "hàn quốc": "Seoul",
    "pháp": "Paris",
    "mỹ": "Washington D.C.",
    "anh": "London"
}

tu_dien_dinh_nghia = {
    "python": "Python là ngôn ngữ lập trình phổ biến nhất thế giới cho AI và phân tích dữ liệu.",
    "ai": "AI (Artificial Intelligence) là Trí tuệ nhân tạo, giúp máy tính có thể suy nghĩ và học hỏi như con người.",
    "robot": "Robot là cỗ máy tự động có thể thực hiện các nhiệm vụ được lập trình sẵn."
}

print("=== CHATBOT TRA CỨU TRI THỨC VÀ PHẢN HỒI TỰ NHIÊN ===")
print("(Thử hỏi: 'chào', 'khen', 'thủ đô của nước...', hoặc định nghĩa 'python là gì', 'ai là gì'...)")
print("(Gõ 'exit' để dừng)\n")

while True:
    cau_hoi = input("Bạn: ").lower().strip()

    if cau_hoi in ["exit", "quit", "thoat", "tạm biệt"]:
        print("Bot: Tạm biệt bạn nhé!")
        break

    if not cau_hoi:
        continue

    # Xử lý chào hỏi ngẫu nhiên bằng random.choice()
    if "chào" in cau_hoi or "hello" in cau_hoi or "hi" in cau_hoi:
        tra_loi = random.choice(danh_sach_chao)
        print(f"Bot: {tra_loi}")

    # Xử lý khen ngợi ngẫu nhiên
    elif "khen" in cau_hoi or "động viên" in cau_hoi:
        tra_loi = random.choice(danh_sach_khen)
        print(f"Bot: {tra_loi}")

    # Tra cứu thủ đô trong Dictionary
    elif "thủ đô" in cau_hoi:
        tim_thay = False
        for quoc_gia, thu_do in tu_dien_thu_do.items():
            if quoc_gia in cau_hoi:
                print(f"Bot: Thủ đô của {quoc_gia.title()} chính là {thu_do} nhé!")
                tim_thay = True
                break
        if not tim_thay:
            print("Bot: Nước này mình chưa có trong danh bạ thủ đô rồi!")

    # Tra cứu định nghĩa công nghệ
    elif "là gì" in cau_hoi or "định nghĩa" in cau_hoi:
        tim_thay = False
        for khai_niem, y_nghia in tu_dien_dinh_nghia.items():
            if khai_niem in cau_hoi:
                print(f"Bot: {y_nghia}")
                tim_thay = True
                break
        if not tim_thay:
            print("Bot: Khái niệm này mình chưa cập nhật vào từ điển tri thức!")

    else:
        print("Bot: Câu này nằm ngoài từ điển dữ liệu của mình rồi!")

# ----------------------------------------------------
# 📝 BÀI TẬP THỰC HÀNH TẠI NHÀ CHO HỌC SINH:
# 1. Thêm 3 quốc gia và thủ đô mới vào `tu_dien_thu_do`.
# 2. Tạo một Dictionary `bang_cuu_chuong` hoặc `tu_dien_tieng_anh` (ví dụ: 'apple': 'quả táo')
#    và thêm tính năng tra từ điển Anh - Việt cho bot.
# ----------------------------------------------------
