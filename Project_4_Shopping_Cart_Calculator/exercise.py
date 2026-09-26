# ==============================================================================
# PROJECT 4: MÁY TÍNH TIỀN HÓA ĐƠN / SHOPPING INVOICE CALCULATOR
# ==============================================================================

# [MỤC TIÊU / GOAL]
# Luyện tập: Hàm (function), Cấu trúc rẽ nhánh (if - elif - else), Vòng lặp (loops), Toán tử số học tính tiền.
# Practice: Functions, Conditional statements (if - elif - else), Loops, Arithmetic operators for pricing.

# [YÊU CẦU ĐỀ BÀI / EXERCISE REQUIREMENTS]
# 1. Viết hàm tinh_tien_mon(don_gia, so_luong) trả về thành tiền = don_gia * so_luong.
# 1. Write a function tinh_tien_mon(don_gia, so_luong) returning item cost = don_gia * so_luong.

# 2. Viết hàm tinh_giam_gia(tong_tien_hang, ma_giam_gia) sử dụng if - elif - else:
# 2. Write a function tinh_giam_gia(tong_tien_hang, ma_giam_gia) using if - elif - else:
#    - Nếu ma_giam_gia == "GIAM10": giảm 10% (tong_tien_hang * 0.10).
#    - If ma_giam_gia == "GIAM10": discount 10% (tong_tien_hang * 0.10).
#    - Nếu ma_giam_gia == "VIP20" và tong_tien_hang >= 200000: giảm 20% (tong_tien_hang * 0.20).
#    - If ma_giam_gia == "VIP20" and tong_tien_hang >= 200000: discount 20% (tong_tien_hang * 0.20).
#    - Ngược lại: không giảm giá (trả về 0).
#    - Otherwise: no discount (return 0).

# 3. Viết hàm tinh_phi_ship(tong_tien_hang) tính phí giao hàng:
# 3. Write a function tinh_phi_ship(tong_tien_hang) calculating shipping fee:
#    - Nếu tong_tien_hang >= 300000: miễn phí ship (0 VND).
#    - If tong_tien_hang >= 300000: free shipping (0 VND).
#    - Nếu tong_tien_hang >= 150000 và < 300000: phí ship là 20000 VND.
#    - If tong_tien_hang >= 150000 and < 300000: shipping fee is 20000 VND.
#    - Nếu tong_tien_hang < 150000: phí ship là 35000 VND.
#    - If tong_tien_hang < 150000: shipping fee is 35000 VND.

# 4. Viết hàm tinh_thue_vat(so_tien_sau_giam, thue_suat=0.08) tính thuế VAT 8%: so_tien_sau_giam * thue_suat.
# 4. Write a function tinh_thue_vat(so_tien_sau_giam, thue_suat=0.08) calculating 8% VAT: so_tien_sau_giam * thue_suat.

# 5. Dùng vòng lặp for hoặc while nhập số lượng các món hàng cần mua, cộng dồn vào tổng tiền hàng.
# 5. Use a for or while loop to input quantities for purchased items, accumulating into total bill.

# 6. In hóa đơn thanh toán chi tiết: Tiền hàng, Tiền giảm giá, Thuế VAT, Phí ship, Tổng thanh toán cuối cùng.
# 6. Print detailed invoice: Subtotal, Discount, VAT tax, Shipping fee, Final total amount.

# ==============================================================================
# [KHUNG BÀI TẬP / STARTER CODE]
# ==============================================================================

def tinh_tien_mon(don_gia, so_luong):
    # Tính thành tiền của 1 món
    # Calculate total cost for one item
    pass

def tinh_giam_gia(tong_tien_hang, ma_giam_gia):
    # Dùng if - elif - else tính số tiền được giảm
    # Use if - elif - else to calculate discount amount
    pass

def tinh_phi_ship(tong_tien_hang):
    # Tính phí giao hàng theo các mức giá
    # Calculate shipping fee by order amount tiers
    pass

def tinh_thue_vat(so_tien_sau_giam, thue_suat=0.08):
    # Tính thuế VAT
    # Calculate VAT tax
    pass

def main():
    # Giá cố định của 3 sản phẩm mẫu
    # Fixed prices for 3 sample products
    gia_banh_mi = 25000
    gia_ca_phe = 30000
    gia_tra_sua = 40000

    # Dùng vòng lặp hoặc nhập số lượng từng món
    # Use loops or input quantity for each item
    pass

if __name__ == "__main__":
    main()
    