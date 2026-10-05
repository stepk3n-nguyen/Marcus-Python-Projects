"""
=============================================================================
CHUYÊN ĐỀ: TẤT TẦN TẬT VỀ HÀM (FUNCTION) TRONG PYTHON TỪ A - Z
Dành cho học sinh & người mới bắt đầu học Lập trình / AI
=============================================================================

MỤC TIÊU BÀI HỌC:
1. Hiểu bản chất của Hàm: Khối mã tái sử dụng, nguyên lý DRY (Don't Repeat Yourself).
2. Nắm vững cú pháp định nghĩa hàm (`def`) và cách gọi hàm (`call function`).
3. Phân biệt Tham số (Parameters) và Đối số (Arguments): Vị trí, Định danh, Mặc định.
4. Hiểu sâu về lệnh `return` và phân biệt rạch ròi giữa `return` với `print()`.
5. Nắm rõ Phạm vi biến: Biến cục bộ (Local) vs Biến toàn cục (Global).
6. Sử dụng kỹ thuật nâng cao: `*args`, `**kwargs`, Hàm ẩn danh (`lambda`).
7. Viết tài liệu chuẩn cho hàm: `Docstring` và Gợi ý kiểu dữ liệu (`Type Hinting`).
8. Thực hành qua các bài tập ứng dụng thực tế từ cơ bản đến chatbot AI.
"""

# =============================================================================
# PHẦN 1: HÀM LÀ GÌ? TẠI SAO CẦN DÙNG HÀM?
# =============================================================================
# - Hàm (Function) giống như một "nhà máy mini" hoặc một "công thức nấu ăn":
#   + Nhận nguyên liệu đầu vào (Input / Tham số).
#   + Chế biến theo quy trình viết sẵn (Xử lý logic).
#   + Xuất ra món ăn hoàn chỉnh (Output / Giá trị trả về qua `return`).
#
# 👉 LỢI ÍCH CỦA HÀM:
#   1. Tránh lặp lại mã nguồn (Nguyên tắc DRY: Don't Repeat Yourself).
#   2. Chia nhỏ bài toán phức tạp thành các phần nhỏ dễ quản lý.
#   3. Dễ bảo trì, sửa lỗi và nâng cấp.

print("=" * 65)
print("PHẦN 1: ĐỊNH NGHĨA VÀ GỌI HÀM CƠ BẢN")
print("=" * 65)

# Cú pháp cơ bản:
# def ten_ham():
#     # Khối lệnh thực thi

def xin_chao():
    """Hàm in lời chào đơn giản không có tham số đầu vào"""
    print("Xin chào các bạn đến với khóa học Python!")

# Gọi hàm (thực thi hàm)
xin_chao()
xin_chao()  # Gọi lại lần 2 mà không cần viết lại lệnh print


# =============================================================================
# PHẦN 2: THAM SỐ (PARAMETERS) VÀ ĐỐI SỐ (ARGUMENTS)
# =============================================================================
# - Parameter (Tham số): Biến được đặt trong ngoặc khi ĐỊNH NGHĨA hàm.
# - Argument (Đối số): Giá trị thực tế truyền vào khi GỌI hàm.

print("\n" + "=" * 65)
print("PHẦN 2: CÁC LOẠI THAM SỐ VÀ ĐỐI SỐ")
print("=" * 65)

# 1. Tham số vị trí (Positional Arguments)
def chao_nguoi_dung(ten, vai_tro):
    print(f"Xin chào {ten}, bạn đang tham gia với vai trò là: {vai_tro}")

# Thứ tự truyền vào quyết định giá trị của biến
chao_nguoi_dung("Nguyễn Văn An", "Học viên")
chao_nguoi_dung("Nghiêm Xuân Sơn", "Giáo viên")


# 2. Đối số định danh (Keyword Arguments)
# Chỉ định rõ tên tham số khi gọi hàm -> không lo bị nhầm thứ tự
chao_nguoi_dung(vai_tro="Giáo viên", ten="Thầy Huy")


# 3. Tham số mặc định (Default Parameters)
# Nếu người gọi không truyền giá trị, Python sẽ lấy giá trị mặc định đã cài sẵn.
# Lưu ý: Tham số mặc định BẮT BUỘC phải đặt ở cuối cùng trong danh sách tham số!
def tao_ho_so(ten, tuoi, quoc_tich="Việt Nam"):
    print(f"Hồ sơ: {ten} | Tuổi: {tuoi} | Quốc tịch: {quoc_tich}")

tao_ho_so("Trần Minh", 12)                    # Dùng quốc tịch mặc định "Việt Nam"
tao_ho_so("John Smith", 15, "Hoa Kỳ")        # Ghi đè quốc tịch thành "Hoa Kỳ"


# =============================================================================
# PHẦN 3: GIÁ TRỊ TRẢ VỀ (RETURN) VS PRINT()
# =============================================================================
# ⚠️ SAI LẦM PHỔ BIẾN CỦA NGƯỜI MỚI HỌC:
#   - `print()`: Chỉ hiển thị chữ ra màn hình console cho mắt người xem.
#   - `return`: Bắn giá trị ra ngoài để lưu vào biến, tính toán tiếp ở các phép tính khác.
#   - Khi gặp lệnh `return`, hàm sẽ DỪNG NGAY LẬP TỨC và thoát ra ngoài.

print("\n" + "=" * 65)
print("PHẦN 3: GIÁ TRỊ TRẢ VỀ VỚI LỆNH RETURN")
print("=" * 65)

# Ví dụ hàm tính tổng 2 số và trả về kết quả
def tinh_tong(a, b):
    tong = a + b
    return tong

ket_qua = tinh_tong(15, 25)
print(f"Tổng 15 + 25 = {ket_qua}")
print(f"Gấp đôi tổng lên: {ket_qua * 2}")  # Nhờ có return mới lấy kết quả nhân 2 được!


# Trả về NHIỀU GIÁ TRỊ cùng lúc (Python sẽ đóng gói thành một Tuple)
def tinh_hinh_chu_nhat(dai, rong):
    chu_vi = (dai + rong) * 2
    dien_tich = dai * rong
    return chu_vi, dien_tich  # Trả về 2 giá trị

cv, dt = tinh_hinh_chu_nhat(10, 5)  # Mở gói (unpacking)
print(f"Hình chữ nhật (10x5) -> Chu vi: {cv}, Diện tích: {dt}")


# =============================================================================
# PHẦN 4: PHẠM VI CỦA BIẾN (VARIABLE SCOPE: LOCAL VS GLOBAL)
# =============================================================================
# - Biến cục bộ (Local Variable): Sinh ra bên trong hàm, ra khỏi hàm sẽ biến mất.
# - Biến toàn cục (Global Variable): Khai báo bên ngoài hàm, dùng được ở mọi nơi.

print("\n" + "=" * 65)
print("PHẦN 4: BIẾN CỤC BỘ VÀ BIẾN TOÀN CỤC")
print("=" * 65)

diem_he_so = 10  # Biến toàn cục (Global)

def kiem_tra_diem():
    diem_cong = 2  # Biến cục bộ (Local)
    tong_diem = diem_he_so + diem_cong
    print(f"Trong hàm: Tổng điểm = {tong_diem}")

kiem_tra_diem()
# print(diem_cong)  # ❌ BÁO LỖI NameError: vì diem_cong chỉ tồn tại trong hàm!

# Sử dụng từ khóa `global` nếu thực sự muốn sửa đổi biến toàn cục bên trong hàm
diem_so = 50

def tang_diem():
    global diem_so
    diem_so += 10

tang_diem()
print("Điểm số sau khi dùng global tăng:", diem_so)


# =============================================================================
# PHẦN 5: THAM SỐ LINH HOẠT (*ARGS VÀ **KWARGS)
# =============================================================================
# - `*args` (Arbitrary Arguments): Nhận số lượng đối số tùy ý dưới dạng Tuple.
# - `**kwargs` (Keyword Arguments): Nhận số lượng tham số đặt tên tùy ý dưới dạng Dictionary.

print("\n" + "=" * 65)
print("PHẦN 5: THAM SỐ LINH HOẠT *ARGS VÀ **KWARGS")
print("=" * 65)

# 1. Dùng *args để tính tổng nhiều số bất kỳ
def tinh_tong_tat_ca(*danh_sach_so):
    print("Dữ liệu args nhận được (Tuple):", danh_sach_so)
    return sum(danh_sach_so)

print("Tổng 3 số:", tinh_tong_tat_ca(1, 2, 3))
print("Tổng 5 số:", tinh_tong_tat_ca(10, 20, 30, 40, 50))


# 2. Dùng **kwargs để nhận thông tin linh hoạt của đối tượng
def thong_tin_tro_ly_ai(**thong_so):
    print("Dữ liệu kwargs nhận được (Dict):", thong_so)
    for khoa, gia_tri in thong_so.items():
        print(f" - {khoa}: {gia_tri}")

thong_tin_tro_ly_ai(ten="Siri", phien_ban=3.5, ngon_ngu="Tiếng Việt", model="Gemini")


# =============================================================================
# PHẦN 6: DOCSTRING VÀ GỢI Ý KIỂU DỮ LIỆU (TYPE HINTING)
# =============================================================================
# - Giúp code chuyên nghiệp, dễ đọc, tự tạo tài liệu khi hover chuột trong IDE.

print("\n" + "=" * 65)
print("PHẦN 6: DOCSTRING VÀ TYPE HINTING CHUYÊN NGHIỆP")
print("=" * 65)

def chia_keo(so_keo: int, so_ban: int) -> tuple[int, int]:
    """
    Chia đều số kẹo cho các bạn và tìm số kẹo còn dư.

    Tham số:
        so_keo (int): Tổng số kẹo có sẵn.
        so_ban (int): Số lượng bạn được chia.

    Trả về:
        tuple[int, int]: (Mỗi bạn được mấy cái kẹo, Số kẹo còn dư).
    """
    keo_moi_ban = so_keo // so_ban
    keo_du = so_keo % so_ban
    return keo_moi_ban, keo_du

moi_ban, du = chia_keo(23, 4)
print(f"23 cái kẹo cho 4 bạn -> Mỗi bạn: {moi_ban} cái, Dư: {du} cái")


# =============================================================================
# PHẦN 7: HÀM ẨN DANH LAMBDA (ANONYMOUS FUNCTION)
# =============================================================================
# - Cú pháp ngắn gọn trên 1 dòng: `lambda tham_so: bieu_thuc`
# - Thích hợp cho các thao tác xử lý nhanh hoặc làm tham số cho hàm khác (sort, map, filter).

print("\n" + "=" * 65)
print("PHẦN 7: HÀM LAMBDA")
print("=" * 65)

# Cách thông thường vs Lambda
binh_phuong = lambda x: x ** 2
print("Bình phương của 6:", binh_phuong(6))

# Ứng dụng sắp xếp danh sách học sinh theo điểm giảm dần bằng Lambda
hoc_sinh_list = [
    {"ten": "An", "diem": 8.5},
    {"ten": "Bình", "diem": 9.2},
    {"ten": "Cường", "diem": 7.8}
]
hoc_sinh_list.sort(key=lambda hs: hs["diem"], reverse=True)
print("Danh sách xếp theo điểm cao xuống thấp:", hoc_sinh_list)


# =============================================================================
# PHẦN 8: BÀI TẬP THỰC HÀNH TỪ CƠ BẢN ĐẾN ỨNG DỤNG AI
# =============================================================================
print("\n" + "=" * 65)
print("PHẦN 8: BÀI TẬP THỰC HÀNH TỰ LUYỆN (CÓ LỜI GIẢI MẪU)")
print("=" * 65)

# --- BÀI TẬP 1: KIỂM TRA SỐ NGUYÊN TỐ ---
# Yêu cầu: Viết hàm kiem_tra_nguyen_to(n) trả về True nếu n là số nguyên tố, ngược lại False.
def kiem_tra_nguyen_to(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("[Bài 1] Số 7 là số nguyên tố?", kiem_tra_nguyen_to(7))
print("[Bài 1] Số 10 là số nguyên tố?", kiem_tra_nguyen_to(10))


# --- BÀI TẬP 2: TÍNH CHỈ SỐ BMI VÀ PHÂN LOẠI SỨC KHỎE ---
# Yêu cầu: Viết hàm tinh_bmi(can_nang, chieu_cao) với chiều cao tính bằng mét.
# Trả về: (chi_so_bmi, phan_loai)
def tinh_bmi(can_nang: float, chieu_cao: float) -> tuple[float, str]:
    bmi = round(can_nang / (chieu_cao ** 2), 2)
    if bmi < 18.5:
        loai = "Gầy (Thiếu cân)"
    elif bmi < 24.9:
        loai = "Bình thường (Lý tưởng)"
    elif bmi < 29.9:
        loai = "Thừa cân"
    else:
        loai = "Béo phì"
    return bmi, loai

bmi, danh_gia = tinh_bmi(55, 1.65)
print(f"[Bài 2] Cân nặng 55kg, Cao 1.65m -> BMI: {bmi} ({danh_gia})")


# --- BÀI TẬP 3: XỬ LÝ DỮ LIỆU TỪ ĐIỂN VÀ THỐNG KÊ LỚP HỌC ---
# Yêu cầu: Viết hàm thong_ke_lop(danh_sach_diem) nhận vào danh sách điểm của học sinh.
# Trả về Dictionary gồm: điểm cao nhất, điểm thấp nhất, điểm trung bình và số lượng học sinh đạt loại Giỏi (>= 8.0).
def thong_ke_lop(diem_so: list[float]) -> dict:
    if not diem_so:
        return {"thong_bao": "Danh sách điểm rỗng"}
    
    dtb = round(sum(diem_so) / len(diem_so), 2)
    gioi_count = sum(1 for d in diem_so if d >= 8.0)
    
    return {
        "so_luong_hs": len(diem_so),
        "diem_cao_nhat": max(diem_so),
        "diem_thap_nhat": min(diem_so),
        "diem_trung_binh": dtb,
        "so_hs_gioi": gioi_count
    }

ket_qua_lop = thong_ke_lop([8.5, 9.0, 7.0, 6.5, 9.5, 8.0, 5.5])
print("[Bài 3] Báo cáo thống kê lớp:", ket_qua_lop)


# --- BÀI TẬP 4: HÀM TIỀN XỬ LÝ TIN NHẮN CHO CHATBOT AI ---
# Yêu cầu: Viết hàm chuan_hoa_va_phan_loai(tin_nhan)
# 1. Chuyển về chữ thường, xóa khoảng trắng thừa ở 2 đầu.
# 2. Phân loại ý định người dùng (Intent Detection): Chào hỏi / Hỏi giờ / Tính toán / Không rõ.
def chuan_hoa_va_phan_loai(tin_nhan: str) -> dict:
    # Bước 1: Làm sạch văn bản (Tiền xử lý NLP cơ bản)
    clean_text = tin_nhan.strip().lower()
    
    # Bước 2: Nhận diện ý định (Intent Recognition)
    if any(tu in clean_text for tu in ["chào", "hello", "hi", "hey"]):
        intent = "chao_hoi"
        phan_hoi = "Chào bạn! Mình có thể giúp gì cho bạn hôm nay?"
    elif any(tu in clean_text for tu in ["giờ", "mấy giờ", "ngày", "thời gian"]):
        intent = "hoi_thoi_gian"
        phan_hoi = "Ý định của bạn là xem thời gian."
    elif any(tu in clean_text for tu in ["tính", "cộng", "trừ", "nhân", "chia", "+", "-", "*", "/"]):
        intent = "tinh_toan"
        phan_hoi = "Ý định của bạn là tính toán biểu thức."
    else:
        intent = "khong_ro"
        phan_hoi = "Xin lỗi, mình chưa hiểu yêu cầu này."

    return {
        "tin_nhan_goc": tin_nhan,
        "tin_nhan_chuan_hoa": clean_text,
        "y_dinh": intent,
        "phan_hoi_goi_y": phan_hoi
    }

print("\n[Bài 4] Demo Intent Bot AI:")
print(chuan_hoa_va_phan_loai("  Xin CHÀO Bot   "))
print(chuan_hoa_va_phan_loai("Hôm nay là mấy giờ rồi?"))
print(chuan_hoa_va_phan_loai("Tính hộ mình 50 * 2"))

print("\n" + "=" * 65)
print("🎉 CHÚC MỪNG BẠN ĐÃ HOÀN THÀNH CHUYÊN ĐỀ FUNCTION TỪ A - Z!")
print("=" * 65)
