# ==============================================================================
# PROJECT 5: TÍNH LƯƠNG & THUẾ THU NHẬP DOANH NGHIỆP / PAYROLL & TAX CALCULATOR
# ==============================================================================

# [MỤC TIÊU / GOAL]
# Nâng cao kỹ năng về hàm (Function):
# - Hàm có tham số mặc định (Default arguments).
# - Hàm gọi lồng nhau (Function calling function).
# - Xử lý tính toán lũy tiến (Progressive tax brackets).
# - Phân tách bài toán lớn thành các hàm nhỏ, độc lập và dễ bảo trì.

# [YÊU CẦU ĐỀ BÀI / REQUIREMENTS]
#
# 1. Viết hàm tinh_luong_chinh(luong_co_ban, so_ngay_cong, ngay_chuan=22):
#    - Lương ngày = luong_co_ban / ngay_chuan.
#    - Lương chính = Lương ngày * so_ngay_cong.
#    - Trả về số tiền lương chính (làm tròn 2 chữ số thập phân).
#
# 2. Viết hàm tinh_tien_tang_ca(so_gio_ot, luong_gio=50000, he_so_ot=1.5):
#    - Tiền OT = so_gio_ot * luong_gio * he_so_ot.
#    - Trả về tiền OT.
#
# 3. Viết hàm tinh_thuong_kpi(luong_co_ban, xep_loai):
#    - Dựa vào xếp loại KPI (A, B, C, D):
#      + "A": Thưởng 30% lương cơ bản (0.30)
#      + "B": Thưởng 15% lương cơ bản (0.15)
#      + "C": Thưởng 5% lương cơ bản (0.05)
#      + "D" hoặc khác: Không có thưởng (0)
#    - Trả về tiền thưởng KPI.
#
# 4. Viết hàm tinh_bao_hiem(luong_dong_bh):
#    - Người lao động đóng: 8% BHXH, 1.5% BHYT, 1% BHTN (Tổng = 10.5%).
#    - Trả về số tiền bảo hiểm khấu trừ = luong_dong_bh * 0.105.
#
# 5. Viết hàm tinh_thue_tncn(tong_thu_nhap, so_nguoi_phu_thuoc=0):
#    - Giảm trừ bản thân: 11,000,000 VND.
#    - Giảm trừ phụ thuộc: 4,400,000 VND / người.
#    - Thu nhập chịu thuế (TNCT) = tong_thu_nhap - 11,000,000 - (so_nguoi_phu_thuoc * 4,400,000).
#    - Nếu TNCT <= 0: Thuế = 0.
#    - Nếu TNCT > 0, tính theo biểu thuế lũy tiến từng phần:
#      + Bậc 1: Đến 5,000,000 VND -> 5%
#      + Bậc 2: Trên 5,000,000 đến 10,000,000 VND -> 10%
#      + Bậc 3: Trên 10,000,000 đến 18,000,000 VND -> 15%
#      + Bậc 4: Trên 18,000,000 VND -> 20%
#    - Trả về số tiền thuế TNCN phải nộp.
#
# 6. Viết hàm main():
#    - Nhập thông tin nhân viên: Tên, Lương cơ bản, Số ngày làm việc, Số giờ OT, Xếp loại KPI (A/B/C/D), Số người phụ thuộc.
#    - Gọi các hàm trên để tính lương thực nhận (Net Salary):
#      Net = Lương chính + Tiền OT + Thưởng KPI - Bảo hiểm - Thuế TNCN
#    - In phiếu lương (Payslip) chi tiết và đẹp mắt.

# ==============================================================================
# [KHUNG BÀI TẬP / STARTER CODE]
# ==============================================================================

def tinh_luong_chinh(luong_co_ban, so_ngay_cong, ngay_chuan=22):
    # TODO: Tính lương chính theo số ngày công thực tế
    pass

def tinh_tien_tang_ca(so_gio_ot, luong_gio=50000, he_so_ot=1.5):
    # TODO: Tính tiền làm thêm giờ (OT)
    pass

def tinh_thuong_kpi(luong_co_ban, xep_loai):
    # TODO: Tính tiền thưởng theo xếp loại A, B, C, D
    pass

def tinh_bao_hiem(luong_dong_bh):
    # TODO: Tính tổng tiền bảo hiểm 10.5% khấu trừ
    pass

def tinh_thue_tncn(tong_thu_nhap, so_nguoi_phu_thuoc=0):
    # TODO: Tính thu nhập chịu thuế và thuế lũy tiến từng phần
    pass

def in_phieu_luong(ten, luong_chinh, tien_ot, thuong_kpi, bao_hiem, thue_tncn, luong_thuc_nhan):
    # TODO: In bảng phiếu lương chi tiết
    pass

def main():
    print("=== HỆ THỐNG QUẢN LÝ & TÍNH LƯƠNG NHÂN VIÊN ===")
    # TODO: Nhập dữ liệu từ người dùng, gọi các hàm và xuất kết quả
    pass

if __name__ == "__main__":
    main()
