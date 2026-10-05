"""
=============================================================================
CHUYÊN ĐỀ: TẤT TẦN TẬT VỀ TỪ ĐIỂN (DICTIONARY) TRONG PYTHON
Dành cho học sinh & người mới bắt đầu học Lập trình / AI
=============================================================================

MỤC TIÊU BÀI HỌC:
1. Hiểu bản chất Dictionary: Cấu trúc Cặp Khóa - Giá trị (Key - Value)
2. Phân biệt được khi nào dùng List và khi nào dùng Dictionary
3. Thành thạo các thao tác cơ bản: Thêm, Sửa, Xóa, Tra cứu dữ liệu (CRUD)
4. Biết cách duyệt Dictionary bằng vòng lặp (keys, values, items)
5. Hiểu Dictionary lồng nhau (Nested Dict) để quản lý dữ liệu phức tạp
6. Ứng dụng Dictionary trong Chatbot và Trí tuệ nhân tạo (AI)
"""

# =============================================================================
# 1. DICTIONARY LÀ GÌ? TẠI SAO CẦN DICTIONARY?
# =============================================================================
# - Trong đời thực: Bạn mở từ điển giấy tìm từ "Apple" -> bạn thấy nghĩa "Quả táo".
# - Trong Python: Dictionary hoạt động y hệt như vậy!
#   + "Key" (Khóa/Từ cần tra)  -> Phải là duy nhất (không trùng lặp)
#   + "Value" (Giá trị/Nghĩa) -> Có thể là bất kỳ kiểu dữ liệu nào (chữ, số, list...)
#
# 👉 So sánh với List:
#   - List: Truy cập bằng CHỈ SỐ THỨ TỰ (0, 1, 2, 3...)
#   - Dictionary: Truy cập bằng TÊN KHÓA (Key) mang ý nghĩa rõ ràng.

print("=" * 60)
print("PHẦN 1: KHỞI TẠO VÀ TRA CỨU DICTIONARY")
print("=" * 60)

# Khởi tạo thông tin một học sinh
hoc_sinh = {
    "ho_ten": "Nguyễn Văn An",
    "tuoi": 13,
    "lop": "7A1",
    "diem_tb": 8.5,
    "la_lop_truong": True
}

# In toàn bộ từ điển
print("Hồ sơ học sinh:", hoc_sinh)

# Cách 1: Truy xuất giá trị bằng cặp ngoặc vuông [key]
print("Tên học sinh:", hoc_sinh["ho_ten"])
print("Lớp:", hoc_sinh["lop"])

# Cách 2: Truy xuất an toàn bằng phương thức .get() (KHUYÊN DÙNG TRONG AI/BOT)
# Nếu key không tồn tại, .get() sẽ trả về giá trị mặc định thay vì báo lỗi dừng chương trình
sdt = hoc_sinh.get("so_dien_thoai", "Chưa cập nhật")
print("Số điện thoại:", sdt)


# =============================================================================
# 2. THÊM, SỬA, XÓA TRONG DICTIONARY
# =============================================================================
print("\n" + "=" * 60)
print("PHẦN 2: THÊM - SỬA - XÓA DỮ LIỆU")
print("=" * 60)

# THÊM MỚI: Chỉ cần gán giá trị cho một Key chưa từng có
hoc_sinh["truong"] = "THCS Newton"
print("Sau khi thêm trường học:", hoc_sinh)

# SỬA/CẬP NHẬT: Gán giá trị mới cho một Key đã tồn tại
hoc_sinh["diem_tb"] = 9.0
print("Sau khi nâng điểm trung bình:", hoc_sinh["diem_tb"])

# CẬP NHẬT NHIỀU KEY CÙNG LÚC: Dùng .update()
hoc_sinh.update({
    "tuoi": 14,
    "chieu_cao": 160
})
print("Sau khi cập nhật tuổi và chiều cao:", hoc_sinh)

# XÓA PHẦN TỬ:
# Cách 1: Dùng lệnh `del`
del hoc_sinh["la_lop_truong"]
print("Sau khi xóa 'la_lop_truong':", hoc_sinh)

# Cách 2: Dùng `.pop(key)` (vừa xóa vừa lấy ra được giá trị bị xóa)
chieu_cao_cu = hoc_sinh.pop("chieu_cao")
print(f"Đã xóa chiều cao ({chieu_cao_cu}cm). Từ điển hiện tại còn:", hoc_sinh)


# =============================================================================
# 3. KIỂM TRA TỒN TẠI VÀ DUYỆT VÒNG LẶP FOR
# =============================================================================
print("\n" + "=" * 60)
print("PHẦN 3: DUYỆT TỪ ĐIỂN VỚI VÒNG LẶP FOR")
print("=" * 60)

tu_dien_thu_do = {
    "việt nam": "Hà Nội",
    "nhật bản": "Tokyo",
    "hàn quốc": "Seoul",
    "pháp": "Paris"
}

# 3.1. Kiểm tra xem 1 quốc gia (Key) có trong từ điển không
quoc_gia_can_tim = "việt nam"
if quoc_gia_can_tim in tu_dien_thu_do:
    print(f"✅ Đã tìm thấy: Thủ đô của {quoc_gia_can_tim.title()} là {tu_dien_thu_do[quoc_gia_can_tim]}")
else:
    print(f"❌ Không tìm thấy dữ liệu về {quoc_gia_can_tim}")

# 3.2. Duyệt qua tất cả các Keys
print("\n--- Danh sách các quốc gia (Keys) ---")
for nuoc in tu_dien_thu_do.keys():
    print("- Quốc gia:", nuoc.title())

# 3.3. Duyệt qua tất cả các Values
print("\n--- Danh sách các thủ đô (Values) ---")
for thu_do in tu_dien_thu_do.values():
    print("- Thủ đô:", thu_do)

# 3.4. Duyệt qua cả cặp Khóa & Giá trị (items()) - CỰC KỲ QUAN TRỌNG!
print("\n--- Bảng tra cứu trọn bộ (Items) ---")
for nuoc, thu_do in tu_dien_thu_do.items():
    print(f"🌍 {nuoc.title():<12} -> 🏛️ {thu_do}")


# =============================================================================
# 4. DICTIONARY LỒNG NHAU (NESTED DICTIONARY)
# =============================================================================
# Trong thực tế, dữ liệu người dùng/sản phẩm thường gồm nhiều tầng thông tin
print("\n" + "=" * 60)
print("PHẦN 4: DICTIONARY NÂNG CAO (NESTED DICTIONARY)")
print("=" * 60)

danh_ba_ai = {
    "tro_ly_siri": {
        "hang": "Apple",
        "nam_ra_doi": 2011,
        "tinh_nang": ["nhận diện giọng nói", "đặt báo thức", "gửi tin nhắn"]
    },
    "tro_ly_gemini": {
        "hang": "Google",
        "nam_ra_doi": 2023,
        "tinh_nang": ["sinh văn bản", "lập trình", "xử lý hình ảnh", "suy luận logic"]
    }
}

# Truy xuất dữ liệu đa tầng:
ten_hang = danh_ba_ai["tro_ly_gemini"]["hang"]
tinh_nang_dau = danh_ba_ai["tro_ly_gemini"]["tinh_nang"][0]
print(f"Gemini là sản phẩm của {ten_hang}, tính năng nổi bật: '{tinh_nang_dau}'")


# =============================================================================
# 5. DEMO ỨNG DỤNG THỰC HÀNH: MINI TỪ ĐIỂN ANH - VIỆT & BỘ ĐẾM TỪ (NLP)
# =============================================================================
print("\n" + "=" * 60)
print("PHẦN 5: DEMO ỨNG DỤNG - ĐẾM TẦN SUẤT TỪ (CƠ SỞ CỦA AI XỬ LÝ NGÔN NGỮ)")
print("=" * 60)

# Trong AI Xử lý Ngôn ngữ Tự nhiên (NLP), máy tính dùng Dictionary để đếm số lần
# mỗi từ xuất hiện trong đoạn văn.
cau_van = "python rất vui và lập trình python rất thú vị lập trình mở ra tương lai"
danh_sach_tu = cau_van.split()

tan_suat_tu = {}
for tu in danh_sach_tu:
    # Nếu từ đã có thì tăng đếm lên 1, nếu chưa có thì gán mặc định là 0 rồi + 1
    tan_suat_tu[tu] = tan_suat_tu.get(tu, 0) + 1

print("Đoạn văn:", cau_van)
print("Thống kê tần suất xuất hiện các từ:")
for tu, so_lan in tan_suat_tu.items():
    print(f" - Từ '{tu}': xuất hiện {so_lan} lần")


# =============================================================================
# 🎯 TỔNG KẾT & BẢNG TRA CỨU NHANH CÁC LỆNH DICTIONARY
# =============================================================================
"""
+-----------------------------+------------------------------------------------------+
| Thao tác                    | Lệnh Python ví dụ                                    |
+-----------------------------+------------------------------------------------------+
| Tạo mới                     | d = {"a": 1, "b": 2} hoặc d = {}                     |
| Lấy giá trị                 | d["a"] hoặc d.get("a", "Mặc định nếu không có")      |
| Thêm / Sửa                  | d["c"] = 3                                           |
| Cập nhật nhiều key          | d.update({"d": 4, "e": 5})                           |
| Xóa phần tử                 | del d["a"] hoặc val = d.pop("a")                     |
| Kiểm tra key có tồn tại     | if "a" in d:                                         |
| Lấy danh sách key           | d.keys()                                             |
| Lấy danh sách value         | d.values()                                           |
| Lấy danh sách (key, value)  | d.items()                                            |
| Đếm số phần tử              | len(d)                                               |
| Xóa sạch từ điển            | d.clear()                                            |
+-----------------------------+------------------------------------------------------+
"""
print("\n🎉 Chúc mừng bạn đã hoàn thành bài học chuyên sâu về Dictionary!")
