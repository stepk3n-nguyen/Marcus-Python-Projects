# ==============================================================================
# PROJECT 7: TÍNH LÃI SUẤT TIẾT KIỆM & LỊCH TRẢ GÓP NGÂN HÀNG / BANK FINANCIAL PLANNER
# LỜI GIẢI HOÀN CHỈNH / FULL SOLUTION
# ==============================================================================

def tinh_lai_tiet_kiem(tien_gui, ky_han_thang, loai_lai="DON"):
    """
    Tính tiền lãi tiết kiệm (Lãi đơn hoặc Lãi kép).
    Trả về: (tien_lai, tong_nhan)
    """
    if ky_han_thang < 6:
        lai_suat_nam = 4.5
    elif ky_han_thang < 12:
        lai_suat_nam = 5.5
    else:
        lai_suat_nam = 6.8

    r = lai_suat_nam / 100

    loai_lai = loai_lai.upper().strip()
    if loai_lai == "KEP":
        # Lãi kép tính gộp lãi theo từng tháng
        tong_nhan = tien_gui * ((1 + r / 12) ** ky_han_thang)
        tien_lai = tong_nhan - tien_gui
    else:
        # Lãi đơn
        tien_lai = tien_gui * r * (ky_han_thang / 12)
        tong_nhan = tien_gui + tien_lai

    return round(tien_lai, 2), round(tong_nhan, 2)

def kiem_tra_du_dieu_kien_vay(thu_nhap_thang, so_tien_tra_hang_thang, co_no_xau=False):
    """
    Thẩm định điều kiện duyệt hồ sơ vay vốn ngân hàng.
    Trả về: (duoc_duyet: bool, ly_do: str)
    """
    if co_no_xau:
        return False, "Hồ sơ bị từ chối do khách hàng có lịch sử nợ xấu (CIC)."

    if thu_nhap_thang <= 0:
        return False, "Thu nhập hàng tháng không hợp lệ."

    dti = so_tien_tra_hang_thang / thu_nhap_thang
    if dti <= 0.60:
        return True, f"Hồ sơ đủ điều kiện! Tỷ lệ trả góp trên thu nhập (DTI): {dti*100:.1f}% <= 60%."
    else:
        return False, f"Hồ sơ bị từ chối vì tỷ lệ DTI ({dti*100:.1f}%) vượt quá ngưỡng an toàn 60%."

def tinh_tra_gop_emi(so_tien_vay, lai_suat_nam, so_thang):
    """
    Tính số tiền trả góp hàng tháng theo công thức Niên kim / EMI cố định.
    Trả về: (emi_thang, tong_tra, tong_lai)
    """
    r_thang = (lai_suat_nam / 100) / 12

    if r_thang == 0:
        emi = so_tien_vay / so_thang
    else:
        # Công thức: EMI = P * [r(1+r)^n] / [(1+r)^n - 1]
        he_so = (1 + r_thang) ** so_thang
        emi = so_tien_vay * (r_thang * he_so) / (he_so - 1)

    tong_tra = emi * so_thang
    tong_lai = tong_tra - so_tien_vay

    return round(emi, 2), round(tong_tra, 2), round(tong_lai, 2)

def in_bang_tra_gop(so_tien_vay, emi_thang, tong_tra, tong_lai, so_thang):
    """In thông tin chi tiết bảng tính vay trả góp."""
    print("\n" + "=" * 55)
    print(f"{'KẾ HOẠCH TRẢ GÓP NGÂN HÀNG (EMI)':^55}")
    print("=" * 55)
    print(f" Số tiền vay gốc:               {so_tien_vay:>15,.0f} VND")
    print(f" Thời hạn vay:                  {so_thang:>15} tháng")
    print("-" * 55)
    print(f" [★] Tiền trả góp mỗi tháng:     {emi_thang:>15,.0f} VND")
    print(f" [+] Tổng tiền lãi trong kỳ:    {tong_lai:>15,.0f} VND")
    print(f" [=] Tổng cả gốc + lãi phải trả:{tong_tra:>15,.0f} VND")
    print("=" * 55 + "\n")

def main():
    while True:
        print("\n" + "=" * 50)
        print("   CHƯƠNG TRÌNH HOẠCH ĐỊNH TÀI CHÍNH NGÂN HÀNG")
        print("=" * 50)
        print(" 1. Tính lãi suất gửi tiết kiệm (Đơn / Kép)")
        print(" 2. Thẩm định & Tính lịch vay trả góp (EMI)")
        print(" 3. Thoát chương trình")
        print("-" * 50)
        chon = input("Vui lòng chọn chức năng (1-3): ").strip()

        if chon == "1":
            print("\n--- TÍNH TIỀN GỬI TIẾT KIỆM ---")
            tien_gui = float(input("Nhập số tiền muốn gửi (VND): "))
            ky_han = int(input("Nhập kỳ hạn gửi (số tháng): "))
            loai_lai = input("Chọn loại lãi (DON: Lãi đơn / KEP: Lãi kép hàng tháng): ")

            tien_lai, tong_nhan = tinh_lai_tiet_kiem(tien_gui, ky_han, loai_lai)
            print("-" * 45)
            print(f" Tiền lãi nhận được:  {tien_lai:>15,.0f} VND")
            print(f" Tổng tiền rút về:    {tong_nhan:>15,.0f} VND")
            print("-" * 45)

        elif chon == "2":
            print("\n--- THẨM ĐỊNH & TÍNH VAY TRẢ GÓP ---")
            thu_nhap = float(input("Nhập thu nhập thực lĩnh hàng tháng (VND): "))
            tien_vay = float(input("Nhập số tiền muốn vay (VND): "))
            lai_suat = float(input("Nhập lãi suất vay (%/năm): "))
            so_thang = int(input("Nhập thời hạn vay (tháng): "))
            
            no_xau_input = input("Có từng có lịch sử nợ xấu ngân hàng không? (y/n): ").strip().lower()
            co_no_xau = (no_xau_input == "y" or no_xau_input == "yes")

            # Tính thử số tiền trả góp hàng tháng
            emi, tong_tra, tong_lai = tinh_tra_gop_emi(tien_vay, lai_suat, so_thang)

            # Thẩm định hồ sơ
            duoc_duyet, thong_diep = kiem_tra_du_dieu_kien_vay(thu_nhap, emi, co_no_xau)

            print("\n" + ">" * 15 + " KẾT QUẢ THẨM ĐỊNH " + "<" * 15)
            if duoc_duyet:
                print(f"✅ {thong_diep}")
                in_bang_tra_gop(tien_vay, emi, tong_tra, tong_lai, so_thang)
            else:
                print(f"❌ {thong_diep}")
                print(f"   (Khoản trả góp dự kiến là {emi:,.0f} VND/tháng so với thu nhập {thu_nhap:,.0f} VND)")

        elif chon == "3":
            print("Cảm ơn bạn đã sử dụng dịch vụ tài chính. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 3.")

if __name__ == "__main__":
    main()
