# ==============================================================================
# PROJECT 4: MÁY TÍNH TIỀN HÓA ĐƠN / SHOPPING INVOICE CALCULATOR
# LỜI GIẢI HOÀN CHỈNH / FULL SOLUTION
# ==============================================================================

# 1. Hàm tính thành tiền của một món hàng
# 1. Function to calculate cost for one item
def tinh_tien_mon(don_gia, so_luong):
    # Dùng toán tử nhân: thành tiền = đơn giá * số lượng
    # Use multiplication operator: item total = unit price * quantity
    thanh_tien = don_gia * so_luong
    return thanh_tien


# 2. Hàm tính số tiền được giảm giá
# 2. Function to calculate discount amount
def tinh_giam_gia(tong_tien_hang, ma_giam_gia):
    # Dùng cấu trúc rẽ nhánh if - elif - else
    # Use conditional structure if - elif - else
    if ma_giam_gia == "GIAM10":
        # Giảm 10% tổng tiền hàng
        # 10% discount on subtotal
        return tong_tien_hang * 0.10
    elif ma_giam_gia == "VIP20" and tong_tien_hang >= 200000:
        # Giảm 20% nếu đơn hàng từ 200,000 VND trở lên
        # 20% discount if order is at least 200,000 VND
        return tong_tien_hang * 0.20
    else:
        # Không đủ điều kiện hoặc mã không hợp lệ
        # Ineligible or invalid voucher code
        return 0.0


# 3. Hàm tính phí vận chuyển theo hạn mức đơn hàng
# 3. Function to calculate tiered shipping fee
def tinh_phi_ship(tong_tien_hang):
    # Đơn hàng từ 300,000 VND trở lên được miễn phí vận chuyển
    # Orders from 300,000 VND and above get free shipping
    if tong_tien_hang >= 300000:
        return 0.0
    # Đơn hàng từ 150,000 VND đến dưới 300,000 VND
    # Orders from 150,000 VND to under 300,000 VND
    elif tong_tien_hang >= 150000:
        return 20000.0
    # Đơn hàng nhỏ dưới 150,000 VND
    # Small orders under 150,000 VND
    else:
        return 35000.0


# 4. Hàm tính thuế VAT 8%
# 4. Function to calculate 8% VAT tax
def tinh_thue_vat(so_tien_sau_giam, thue_suat=0.08):
    # Dùng toán tử nhân tính thuế trên số tiền sau khi đã trừ giảm giá
    # Use multiplication to calculate tax on amount after discount
    tien_thue = so_tien_sau_giam * thue_suat
    return tien_thue


# 5. Hàm chính thực thi chương trình
# 5. Main function to execute program
def main():
    print("=== CỬA HÀNG THỰC PHẨM & ĐỒ UỐNG MARCUS ===")
    print("=== MARCUS FOOD & DRINKS STORE ===")

    # Bảng giá niêm yết của 3 món hàng
    # Price list of 3 items
    gia_banh_mi = 25000
    gia_ca_phe = 30000
    gia_tra_sua = 40000

    print("\n--- MENU SẢN PHẨM / PRODUCT MENU ---")
    print(f"1. Bánh mì / Banh Mi: {gia_banh_mi} VND")
    print(f"2. Cà phê sữa / Milk Coffee: {gia_ca_phe} VND")
    print(f"3. Trà sữa trân châu / Bubble Tea: {gia_tra_sua} VND")

    # Nhập số lượng từng món từ bàn phím
    # Input quantity for each item from keyboard
    sl_banh_mi = int(input("\nNhập số lượng Bánh mì muốn mua / Enter Banh Mi quantity: "))
    sl_ca_phe = int(input("Nhập số lượng Cà phê muốn mua / Enter Coffee quantity: "))
    sl_tra_sua = int(input("Nhập số lượng Trà sữa muốn mua / Enter Bubble Tea quantity: "))

    # Tính tiền từng món bằng hàm
    # Calculate each item cost using function
    tien_banh_mi = tinh_tien_mon(gia_banh_mi, sl_banh_mi)
    tien_ca_phe = tinh_tien_mon(gia_ca_phe, sl_ca_phe)
    tien_tra_sua = tinh_tien_mon(gia_tra_sua, sl_tra_sua)

    # Tính tổng tiền hàng bằng toán tử cộng
    # Calculate subtotal using addition operator
    tong_tien_hang = tien_banh_mi + tien_ca_phe + tien_tra_sua

    # Nhập mã giảm giá
    # Input voucher code
    print("\n(Gợi ý mã giảm giá: GIAM10, VIP20)")
    print("(Discount code hints: GIAM10, VIP20)")
    ma_voucher = input("Nhập mã giảm giá của bạn / Enter voucher code: ")

    # Tính các khoản tiền theo hàm
    # Calculate fees and deductions using functions
    tien_giam = tinh_giam_gia(tong_tien_hang, ma_voucher)
    tien_sau_giam = tong_tien_hang - tien_giam
    tien_vat = tinh_thue_vat(tien_sau_giam, 0.08)
    phi_ship = tinh_phi_ship(tong_tien_hang)

    # Tính tổng thanh toán cuối cùng
    # Calculate final total payment
    tong_thanh_toan = tien_sau_giam + tien_vat + phi_ship

    # In hóa đơn chi tiết
    # Print detailed invoice
    print("\n=============================================")
    print("          HÓA ĐƠN BÁN HÀNG / INVOICE         ")
    print("=============================================")
    print(f"Bánh mì ({sl_banh_mi} cái)       : {tien_banh_mi} VND")
    print(f"Cà phê ({sl_ca_phe} ly)         : {tien_ca_phe} VND")
    print(f"Trà sữa ({sl_tra_sua} ly)        : {tien_tra_sua} VND")
    print("---------------------------------------------")
    print(f"Tổng tiền hàng (Subtotal)    : {tong_tien_hang} VND")
    print(f"Tiền giảm giá (Discount)     : -{tien_giam} VND")
    print(f"Thuế VAT 8% (VAT Tax)        : +{tien_vat} VND")
    print(f"Phí giao hàng (Shipping)     : +{phi_ship} VND")
    print("=============================================")
    print(f"TỔNG THANH TOÁN (FINAL TOTAL): {tong_thanh_toan} VND")
    print("=============================================")
    print("Cảm ơn quý khách và hẹn gặp lại!")
    print("Thank you and see you again!")


if __name__ == "__main__":
    main()
