# ==============================================================================
# PROJECT 7: TÍNH LÃI SUẤT TIẾT KIỆM & LỊCH TRẢ GÓP NGÂN HÀNG / BANK FINANCIAL PLANNER
# ==============================================================================

# [MỤC TIÊU / GOAL]
# Nâng cao tư duy xây dựng hàm và xử lý công thức toán học/tài chính trong lập trình:
# - Hàm trả về nhiều giá trị (Return multiple values / Tuple).
# - Vận dụng công thức toán học phức tạp (Lũy thừa, Lãi kép, Niên kim cố định EMI).
# - Xây dựng hệ thống menu đa chức năng lồng các hàm điều phối.

# [YÊU CẦU ĐỀ BÀI / REQUIREMENTS]
#
# 1. Viết hàm tinh_lai_tiet_kiem(tien_gui, ky_han_thang, loai_lai="DON"):
#    - Bảng lãi suất năm theo kỳ hạn:
#      + Dưới 6 tháng: 4.5% / năm
#      + Từ 6 đến dưới 12 tháng: 5.5% / năm
#      + Từ 12 tháng trở lên: 6.8% / năm
#    - Lãi đơn (loai_lai == "DON"):
#      + Tien_lai = tien_gui * (lai_suat_nam / 100) * (ky_han_thang / 12)
#      + Tong_nhan = tien_gui + tien_lai
#    - Lãi kép hàng tháng (loai_lai == "KEP"):
#      + Tong_nhan = tien_gui * (1 + (lai_suat_nam / 100) / 12) ** ky_han_thang
#      + Tien_lai = Tong_nhan - tien_gui
#    - Trả về 2 giá trị: (tien_lai, tong_nhan).
#
# 2. Viết hàm kiem_tra_du_dieu_kien_vay(thu_nhap_thang, so_tien_tra_hang_thang, co_no_xau=False):
#    - Nếu co_no_xau == True -> Từ chối vay (False, "Lý do: Khách hàng có lịch sử nợ xấu").
#    - Tỷ lệ trả nợ trên thu nhập (DTI - Debt-to-Income):
#      + Ty_le = so_tien_tra_hang_thang / thu_nhap_thang
#      + Nếu ty_le <= 0.60 (khoản trả góp <= 60% thu nhập): Đủ điều kiện (True, "Đủ điều kiện vay vốn")
#      + Nếu ty_le > 0.60: Không đủ điều kiện (False, "Lý do: Khoản trả hàng tháng vượt quá 60% thu nhập").
#    - Trả về tuple: (trang_thai_bool, ly_do_str).
#
# 3. Viết hàm tinh_tra_gop_emi(so_tien_vay, lai_suat_nam, so_thang):
#    - Tính số tiền cố định phải trả đều mỗi tháng (công thức EMI chuẩn ngân hàng):
#      + r = (lai_suat_nam / 100) / 12 (lãi suất theo tháng)
#      + EMI = so_tien_vay * [r * (1 + r)^so_thang] / [(1 + r)^so_thang - 1]
#    - Tổng tiền phải trả = EMI * so_thang.
#    - Tổng tiền lãi phải trả = Tổng tiền phải trả - so_tien_vay.
#    - Trả về 3 giá trị: (emi_thang, tong_tra, tong_lai).
#
# 4. Viết hàm in_bang_tra_gop(so_tien_vay, emi_thang, tong_tra, tong_lai, so_thang):
#    - In bảng kế hoạch tài chính trả góp rõ ràng, định dạng tiền tệ.
#
# 5. Viết hàm main():
#    - Hiển thị menu cho người dùng chọn:
#      1. Tính tiền gửi tiết kiệm (Lãi đơn / Lãi kép).
#      2. Thẩm định điều kiện vay & Tính lịch trả góp hàng tháng.
#      3. Thoát chương trình.
#    - Dùng vòng lặp while để giữ chương trình chạy cho đến khi chọn thoát.

# ==============================================================================
# [KHUNG BÀI TẬP / STARTER CODE]
# ==============================================================================

def tinh_lai_tiet_kiem(tien_gui, ky_han_thang, loai_lai="DON"):
    # TODO: Tính tiền lãi và tổng tiền nhận được theo kỳ hạn và loại lãi
    pass

def kiem_tra_du_dieu_kien_vay(thu_nhap_thang, so_tien_tra_hang_thang, co_no_xau=False):
    # TODO: Thẩm định hồ sơ vay dựa trên nợ xấu và tỷ lệ DTI
    pass

def tinh_tra_gop_emi(so_tien_vay, lai_suat_nam, so_thang):
    # TODO: Tính tiền trả góp cố định hàng tháng theo công thức EMI
    pass

def in_bang_tra_gop(so_tien_vay, emi_thang, tong_tra, tong_lai, so_thang):
    # TODO: In bảng kế hoạch trả nợ
    pass

def main():
    # TODO: Xây dựng menu lựa chọn và gọi các hàm tương ứng
    pass

if __name__ == "__main__":
    main()
