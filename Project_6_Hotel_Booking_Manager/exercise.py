# ==============================================================================
# PROJECT 6: QUẢN LÝ ĐẶT PHÒNG & DỊCH VỤ KHÁCH SẠN / HOTEL BOOKING MANAGER
# ==============================================================================

# [MỤC TIÊU / GOAL]
# Luyện tập kỹ năng hàm nâng cao:
# - Hàm kiểm tra và xác thực dữ liệu đầu vào (Input Validation function).
# - Hàm tính toán tổ hợp dịch vụ với nhiều tham số tùy chọn (Keyword arguments / Default values).
# - Áp dụng các mức chiết khấu thành viên và phụ thu cao điểm.

# [YÊU CẦU ĐỀ BÀI / REQUIREMENTS]
#
# 1. Viết hàm lay_gia_phong(loai_phong):
#    - "STANDARD": 500,000 VND / đêm
#    - "DELUXE":   900,000 VND / đêm
#    - "SUITE":    1,600,000 VND / đêm
#    - "VIP":      2,500,000 VND / đêm
#    - Nếu nhập sai loại phòng, trả về -1 để báo lỗi.
#
# 2. Viết hàm tinh_tien_phong(don_gia_phong, so_dem, la_ngay_le=False):
#    - Tiền phòng gốc = don_gia_phong * so_dem.
#    - Nếu là ngày lễ (la_ngay_le=True): Phụ thu thêm 25% (nhân hệ số 1.25).
#    - Trả về tổng tiền phòng.
#
# 3. Viết hàm tinh_tien_dich_vu(so_nguoi, so_bua_buffet=0, don_san_bay=False, giat_ui=False):
#    - Buffet sáng: 120,000 VND / người / bữa. (Tiền = so_nguoi * so_bua_buffet * 120000)
#    - Đón sân bay: 350,000 VND trọn gói chuyến (nếu don_san_bay=True).
#    - Giặt ủi: 150,000 VND trọn gói (nếu giat_ui=True).
#    - Trả về tổng tiền các dịch vụ phát sinh.
#
# 4. Viết hàm tinh_giam_gia_thanh_vien(tong_chi_phi, hang_the="STANDARD"):
#    - Hạng thẻ thành viên:
#      + "SILVER": Giảm 5% tổng chi phí.
#      + "GOLD": Giảm 10% tổng chi phí.
#      + "PLATINUM": Giảm 15% tổng chi phí.
#      + "STANDARD" hoặc khác: Không giảm giá (0 VND).
#    - Trả về số tiền được giảm giá.
#
# 5. Viết hàm main():
#    - Yêu cầu người dùng nhập thông tin đặt phòng: Tên khách hàng, Loại phòng, Số đêm, Số người.
#    - Kiểm tra loại phòng hợp lệ hay không (nếu không hợp lệ thì thông báo và dừng).
#    - Hỏi xem có phải dịp ngày lễ không (y/n).
#    - Hỏi các dịch vụ đi kèm: số bữa buffet, có đón sân bay không (y/n), có giặt ủi không (y/n).
#    - Nhập hạng thẻ thành viên.
#    - Tính toán và in Hóa đơn thanh toán khách sạn (Hotel Booking Invoice) chi tiết.

# ==============================================================================
# [KHUNG BÀI TẬP / STARTER CODE]
# ==============================================================================

def lay_gia_phong(loai_phong):
    # TODO: Trả về giá phòng tương ứng hoặc -1 nếu không hợp lệ
    pass

def tinh_tien_phong(don_gia_phong, so_dem, la_ngay_le=False):
    # TODO: Tính tiền phòng có tính phụ thu ngày lễ nếu có
    pass

def tinh_tien_dich_vu(so_nguoi, so_bua_buffet=0, don_san_bay=False, giat_ui=False):
    # TODO: Tính tổng chi phí các dịch vụ kèm theo
    pass

def tinh_giam_gia_thanh_vien(tong_chi_phi, hang_the="STANDARD"):
    # TODO: Tính số tiền chiết khấu theo hạng thẻ thành viên
    pass

def in_hoa_don_khach_san(ten_khach, loai_phong, so_dem, tien_phong, tien_dv, giam_gia, vat, tong_cong):
    # TODO: In hóa đơn thanh toán khách sạn
    pass

def main():
    print("=== HỆ THỐNG ĐẶT PHÒNG KHÁCH SẠN / HOTEL BOOKING ===")
    # TODO: Thực hiện luồng nhập liệu, gọi hàm và in hóa đơn
    pass

if __name__ == "__main__":
    main()
