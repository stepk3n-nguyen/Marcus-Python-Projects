"""
BÀI 02: BIẾN SỐ, KIỂU DỮ LIỆU & PHÉP TOÁN
Dành cho học sinh lớp 7

Mục tiêu:
- Hiểu khái niệm Biến (Variable) - như một chiếc hộp lưu trữ dữ liệu
- Nắm được 3 kiểu dữ liệu cốt lõi: int (số nguyên), float (số thực/thập phân), str (chuỗi chữ)
- Chuyển đổi kiểu dữ liệu bằng int() và float() khi dùng input()
- Thực hành làm "Máy Tính Thông Minh Mini"
"""

# ----------------------------------------------------
# 1. BIẾN VÀ CÁC KIỂU DỮ LIỆU
# ----------------------------------------------------
ten_bot = "AI-Kid 7"     # Kiểu str (String - Chuỗi chữ)
nam_sinh = 2026          # Kiểu int (Integer - Số nguyên)
diem_toan = 9.5          # Kiểu float (Số thực / số thập phân)
trang_thai = True        # Kiểu bool (Đúng/Sai)

print(f"Xin chào, tôi là {ten_bot}. Điểm trung bình mẫu: {diem_toan}")

# ----------------------------------------------------
# 2. CÁC PHÉP TOÁN CƠ BẢN TRONG PYTHON
# ----------------------------------------------------
a = 15
b = 4

print(f"Tổng: {a} + {b} = {a + b}")
print(f"Hiệu: {a} - {b} = {a - b}")
print(f"Tích: {a} * {b} = {a * b}")
print(f"Thương (chia thường): {a} / {b} = {a / b}")
print(f"Chia lấy phần nguyên: {a} // {b} = {a // b}")
print(f"Chia lấy phần dư: {a} % {b} = {a % b}")
print(f"Lũy thừa ({a} mũ {b}): {a} ** {b} = {a ** b}")


# ----------------------------------------------------
# 3. MINI PROJECT: MÁY TÍNH HỌC TẬP THÔNG MINH
# ----------------------------------------------------
print("\n=== MÁY TÍNH HỌC TẬP THÔNG MINH LỚP 7 ===")
# Lưu ý quan trọng: Lệnh input() luôn trả về kiểu chữ (str), 
# nên cần bọc float() hoặc int() để tính toán số học.

so_thu_nhat = float(input("Nhập số thứ nhất: "))
so_thu_hai = float(input("Nhập số thứ hai: "))

print("\n--- KẾT QUẢ TÍNH TOÁN ---")
print(f"Cộng: {so_thu_nhat} + {so_thu_hai} = {so_thu_nhat + so_thu_hai}")
print(f"Trừ:  {so_thu_nhat} - {so_thu_hai} = {so_thu_nhat - so_thu_hai}")
print(f"Nhân: {so_thu_nhat} * {so_thu_hai} = {so_thu_nhat * so_thu_hai}")

if so_thu_hai != 0:
    print(f"Chia: {so_thu_nhat} / {so_thu_hai} = {round(so_thu_nhat / so_thu_hai, 2)}")
else:
    print("Chia: Không thể chia cho số 0!")

# ----------------------------------------------------
# 📝 BÀI TẬP THỰC HÀNH TẠI NHÀ CHO HỌC SINH:
# 1. Viết chương trình tính chu vi và diện tích hình chữ nhật khi người dùng nhập chiều dài, chiều rộng.
# 2. Viết chương trình tính tuổi của người dùng: Nhập năm sinh -> Tính tuổi đến năm hiện tại.
# ----------------------------------------------------
