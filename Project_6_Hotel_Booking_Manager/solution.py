# ==============================================================================
# PROJECT 6: QUẢN LÝ ĐẶT PHÒNG & DỊCH VỤ KHÁCH SẠN / HOTEL BOOKING MANAGER
# LỜI GIẢI HOÀN CHỈNH / FULL SOLUTION
# ==============================================================================

def lay_gia_phong(loai_phong):
    """Lấy đơn giá phòng theo đêm. Trả về -1 nếu loại phòng không hợp lệ."""
    loai_phong = loai_phong.upper().strip()
    bang_gia = {
        "STANDARD": 500000,
        "DELUXE": 900000,
        "SUITE": 1600000,
        "VIP": 2500000
    }
    return bang_gia.get(loai_phong, -1)

def tinh_tien_phong(don_gia_phong, so_dem, la_ngay_le=False):
    """Tính tiền phòng cơ bản có tính thêm phụ thu nếu vào dịp lễ Tết."""
    tien_goc = don_gia_phong * so_dem
    if la_ngay_le:
        return round(tien_goc * 1.25, 2)
    return round(tien_goc, 2)

def tinh_tien_dich_vu(so_nguoi, so_bua_buffet=0, don_san_bay=False, giat_ui=False):
    """Tính tổng chi phí các dịch vụ bổ sung dựa trên lựa chọn của khách."""
    gia_buffet_don = 120000
    gia_don_san_bay = 350000
    gia_giat_ui = 150000
    
    tien_buffet = so_nguoi * so_bua_buffet * gia_buffet_don
    tien_xe = gia_don_san_bay if don_san_bay else 0
    tien_giat = gia_giat_ui if giat_ui else 0
    
    return tien_buffet + tien_xe + tien_giat

def tinh_giam_gia_thanh_vien(tong_chi_phi, hang_the="STANDARD"):
    """Tính mức giảm giá dựa trên cấp bậc thành viên loyalty."""
    hang_the = hang_the.upper().strip()
    if hang_the == "PLATINUM":
        ti_le = 0.15
    elif hang_the == "GOLD":
        ti_le = 0.10
    elif hang_the == "SILVER":
        ti_le = 0.05
    else:
        ti_le = 0.0
        
    return round(tong_chi_phi * ti_le, 2)

def in_hoa_don_khach_san(ten_khach, loai_phong, so_dem, tien_phong, tien_dv, giam_gia, vat, tong_cong):
    """In hóa đơn chi tiết khách sạn."""
    print("\n" + "=" * 55)
    print(f"{'HÓA ĐƠN ĐẶT PHÒNG KHÁCH SẠN':^55}")
    print("=" * 55)
    print(f" Khách hàng: {ten_khach}")
    print(f" Loại phòng: {loai_phong.upper()} ({so_dem} đêm)")
    print("-" * 55)
    print(f" [+] Tiền phòng:                {tien_phong:>15,.0f} VND")
    print(f" [+] Dịch vụ bổ sung:           {tien_dv:>15,.0f} VND")
    print(f" [-] Giảm giá thành viên:       {giam_gia:>15,.0f} VND")
    print(f" [+] Thuế VAT & Phí DV (8%):    {vat:>15,.0f} VND")
    print("=" * 55)
    print(f" [★] TỔNG CỘNG THANH TOÁN:      {tong_cong:>15,.0f} VND")
    print("=" * 55 + "\n")

def main():
    print("=== HỆ THỐNG ĐẶT PHÒNG KHÁCH SẠN / HOTEL BOOKING ===")
    
    ten_khach = input("Nhập tên khách hàng: ")
    loai_phong = input("Chọn loại phòng (STANDARD / DELUXE / SUITE / VIP): ")
    
    don_gia = lay_gia_phong(loai_phong)
    if don_gia == -1:
        print("❌ Lỗi: Loại phòng bạn nhập không tồn tại trong hệ thống!")
        return
    
    so_dem = int(input("Nhập số đêm lưu trú: "))
    so_nguoi = int(input("Nhập số lượng khách ở: "))
    
    la_le_input = input("Có phải thời gian ngày lễ/Tết không? (y/n): ").strip().lower()
    la_ngay_le = (la_le_input == "y" or la_le_input == "yes")
    
    print("\n--- Dịch vụ bổ sung ---")
    so_bua_buffet = int(input("Số bữa ăn sáng Buffet đăng ký: "))
    don_sb_input = input("Đăng ký xe đón sân bay không? (y/n): ").strip().lower()
    don_san_bay = (don_sb_input == "y" or don_sb_input == "yes")
    
    giat_ui_input = input("Đăng ký gói giặt ủi đồ không? (y/n): ").strip().lower()
    giat_ui = (giat_ui_input == "y" or giat_ui_input == "yes")
    
    hang_the = input("Hạng thẻ thành viên (STANDARD / SILVER / GOLD / PLATINUM): ")
    
    # Tính toán
    tien_phong = tinh_tien_phong(don_gia, so_dem, la_ngay_le)
    tien_dv = tinh_tien_dich_vu(so_nguoi, so_bua_buffet, don_san_bay, giat_ui)
    tong_tam_tinh = tien_phong + tien_dv
    
    giam_gia = tinh_giam_gia_thanh_vien(tong_tam_tinh, hang_the)
    sau_giam = tong_tam_tinh - giam_gia
    
    vat = round(sau_giam * 0.08, 2)
    tong_cong = sau_giam + vat
    
    in_hoa_don_khach_san(ten_khach, loai_phong, so_dem, tien_phong, tien_dv, giam_gia, vat, tong_cong)

if __name__ == "__main__":
    main()
