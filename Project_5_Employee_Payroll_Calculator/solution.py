# ==============================================================================
# PROJECT 5: TÍNH LƯƠNG & THUẾ THU NHẬP DOANH NGHIỆP / PAYROLL & TAX CALCULATOR
# LỜI GIẢI HOÀN CHỈNH / FULL SOLUTION
# ==============================================================================

def tinh_luong_chinh(luong_co_ban, so_ngay_cong, ngay_chuan=22):
    """Tính lương chính dựa trên số ngày làm việc thực tế so với ngày chuẩn."""
    luong_ngay = luong_co_ban / ngay_chuan
    luong_chinh = luong_ngay * so_ngay_cong
    return round(luong_chinh, 2)

def tinh_tien_tang_ca(so_gio_ot, luong_gio=50000, he_so_ot=1.5):
    """Tính tiền làm thêm giờ (OT) với hệ số nhân."""
    tien_ot = so_gio_ot * luong_gio * he_so_ot
    return round(tien_ot, 2)

def tinh_thuong_kpi(luong_co_ban, xep_loai):
    """Tính tiền thưởng KPI dựa trên đánh giá A, B, C, D."""
    xep_loai = xep_loai.upper().strip()
    if xep_loai == "A":
        ti_le = 0.30
    elif xep_loai == "B":
        ti_le = 0.15
    elif xep_loai == "C":
        ti_le = 0.05
    else:
        ti_le = 0.0
    
    return round(luong_co_ban * ti_le, 2)

def tinh_bao_hiem(luong_dong_bh):
    """Tính 10.5% các loại bảo hiểm bắt buộc (BHXH 8%, BHYT 1.5%, BHTN 1%)."""
    ti_le_bh = 0.105
    return round(luong_dong_bh * ti_le_bh, 2)

def tinh_thue_tncn(tong_thu_nhap, so_nguoi_phu_thuoc=0):
    """Tính thuế TNCN theo biểu thuế lũy tiến từng phần chuẩn."""
    giam_tru_ban_than = 11000000
    giam_tru_phu_thuoc = so_nguoi_phu_thuoc * 4400000
    
    # Thu nhập chịu thuế
    tnct = tong_thu_nhap - giam_tru_ban_than - giam_tru_phu_thuoc
    
    if tnct <= 0:
        return 0.0
    
    thue = 0.0
    # Bậc 1: <= 5,000,000 (5%)
    if tnct <= 5000000:
        thue = tnct * 0.05
    # Bậc 2: > 5tr đến 10tr (10%)
    elif tnct <= 1000000:
        thue = (5000000 * 0.05) + (tnct - 5000000) * 0.10
    # Bậc 3: > 10tr đến 18tr (15%)
    elif tnct <= 18000000:
        thue = (5000000 * 0.05) + (5000000 * 0.10) + (tnct - 10000000) * 0.15
    # Bậc 4: > 18tr (20%)
    else:
        thue = (5000000 * 0.05) + (5000000 * 0.10) + (8000000 * 0.15) + (tnct - 18000000) * 0.20
        
    return round(thue, 2)

def in_phieu_luong(ten, luong_chinh, tien_ot, thuong_kpi, bao_hiem, thue_tncn, luong_thuc_nhan):
    """In định dạng phiếu lương rõ ràng, chuyên nghiệp."""
    print("\n" + "=" * 50)
    print(f"{'PHIẾU LƯƠNG NHÂN VIÊN':^50}")
    print("=" * 50)
    print(f" Nhân viên: {ten}")
    print("-" * 50)
    print(f" [+] Lương chính thực tế:       {luong_chinh:>15,.0f} VND")
    print(f" [+] Tiền làm thêm giờ (OT):    {tien_ot:>15,.0f} VND")
    print(f" [+] Thưởng hiệu suất (KPI):    {thuong_kpi:>15,.0f} VND")
    tong_thu_nhap = luong_chinh + tien_ot + thuong_kpi
    print(f"  -> Tổng thu nhập:             {tong_thu_nhap:>15,.0f} VND")
    print("-" * 50)
    print(f" [-] Bảo hiểm (10.5%):          {bao_hiem:>15,.0f} VND")
    print(f" [-] Thuế TNCN tạm tính:        {thue_tncn:>15,.0f} VND")
    print("=" * 50)
    print(f" [★] LƯƠNG THỰC NHẬN (NET):     {luong_thuc_nhan:>15,.0f} VND")
    print("=" * 50 + "\n")

def main():
    print("=== HỆ THỐNG QUẢN LÝ & TÍNH LƯƠNG NHÂN VIÊN ===")
    
    ten = input("Nhập họ tên nhân viên: ")
    luong_co_ban = float(input("Nhập mức lương cơ bản (VND): "))
    so_ngay_cong = float(input("Nhập số ngày công làm việc (chuẩn 22 ngày): "))
    so_gio_ot = float(input("Nhập số giờ làm thêm (OT): "))
    xep_loai_kpi = input("Nhập xếp loại KPI (A / B / C / D): ")
    so_nguoi_phu_thuoc = int(input("Nhập số người phụ thuộc giảm trừ gia cảnh: "))
    
    # 1. Tính toán các khoản thu nhập
    luong_chinh = tinh_luong_chinh(luong_co_ban, so_ngay_cong)
    tien_ot = tinh_tien_tang_ca(so_gio_ot, luong_gio=luong_co_ban / (22 * 8), he_so_ot=1.5)
    thuong_kpi = tinh_thuong_kpi(luong_co_ban, xep_loai_kpi)
    tong_thu_nhap = luong_chinh + tien_ot + thuong_kpi
    
    # 2. Tính toán các khoản khấu trừ
    bao_hiem = tinh_bao_hiem(luong_co_ban)
    thue_tncn = tinh_thue_tncn(tong_thu_nhap, so_nguoi_phu_thuoc)
    
    # 3. Lương thực nhận (Net)
    luong_thuc_nhan = tong_thu_nhap - bao_hiem - thue_tncn
    
    # 4. Xuất phiếu lương
    in_phieu_luong(ten, luong_chinh, tien_ot, thuong_kpi, bao_hiem, thue_tncn, luong_thuc_nhan)

if __name__ == "__main__":
    main()
