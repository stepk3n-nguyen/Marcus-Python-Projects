# ==============================================================================
# PROJECT 6: QUẢN LÝ ĐẶT PHÒNG & DỊCH VỤ KHÁCH SẠN / HOTEL BOOKING MANAGER
# ==============================================================================

# ------------------------------------------------------------------------------
# [TIẾNG VIỆT] ĐỀ BÀI: QUẢN LÝ ĐẶT PHÒNG KHÁCH SẠN
# ------------------------------------------------------------------------------
# MỤC TIÊU:
# Luyện tập nâng cao về Hàm:
# - Hàm kiểm tra và xác thực dữ liệu đầu vào (Input validation function).
# - Hàm tính toán tổ hợp dịch vụ với nhiều tham số tùy chọn (Keyword arguments / Boolean flags).
# - Áp dụng các mức chiết khấu thành viên và phụ thu cao điểm.
#
# YÊU CẦU:
# 1. Viết hàm get_room_price(room_type):
#    - "STANDARD": 500,000 VND / đêm
#    - "DELUXE":   900,000 VND / đêm
#    - "SUITE":    1,600,000 VND / đêm
#    - "VIP":      2,500,000 VND / đêm
#    - Nếu nhập sai loại phòng, trả về -1 để báo lỗi.
#
# 2. Viết hàm calculate_room_cost(room_price, nights, is_holiday=False):
#    - Tiền phòng gốc = room_price * nights.
#    - Nếu là ngày lễ (is_holiday=True): Phụ thu thêm 25% (nhân 1.25).
#    - Trả về tổng tiền phòng.
#
# 3. Viết hàm calculate_service_cost(guests_count, buffet_meals=0, airport_pickup=False, laundry=False):
#    - Buffet sáng: 120,000 VND / khách / bữa. (Tiền = guests_count * buffet_meals * 120000)
#    - Đón sân bay: 350,000 VND trọn gói (nếu airport_pickup=True).
#    - Giặt ủi: 150,000 VND trọn gói (nếu laundry=True).
#    - Trả về tổng chi phí các dịch vụ phát sinh.
#
# 4. Viết hàm calculate_membership_discount(subtotal, membership_tier="STANDARD"):
#    - Hạng thẻ thành viên:
#      + "SILVER": Giảm 5% tổng chi phí.
#      + "GOLD": Giảm 10% tổng chi phí.
#      + "PLATINUM": Giảm 15% tổng chi phí.
#      + "STANDARD" hoặc khác: Không giảm giá (0 VND).
#    - Trả về số tiền được giảm giá.
#
# 5. Viết hàm main():
#    - Nhập thông tin: Tên khách hàng, Loại phòng, Số đêm, Số lượng khách.
#    - Kiểm tra loại phòng hợp lệ, nếu không hợp lệ thì báo lỗi và dừng chương trình.
#    - Hỏi xem có phải dịp ngày lễ không (y/n).
#    - Hỏi các dịch vụ đi kèm: số bữa buffet, có đón sân bay không (y/n), có giặt ủi không (y/n).
#    - Nhập hạng thẻ thành viên.
#    - Tính thuế VAT 8% và in Hóa đơn thanh toán chi tiết.

# ------------------------------------------------------------------------------
# [ENGLISH] EXERCISE: HOTEL BOOKING & SERVICE MANAGER
# ------------------------------------------------------------------------------
# GOALS:
# Advanced function practice:
# - Input validation functions.
# - Multi-service calculations using keyword arguments and boolean flags.
# - Peak season surcharges and membership loyalty discounts.
#
# REQUIREMENTS:
# 1. Write get_room_price(room_type):
#    - "STANDARD": 500,000 VND / night
#    - "DELUXE":   900,000 VND / night
#    - "SUITE":    1,600,000 VND / night
#    - "VIP":      2,500,000 VND / night
#    - If invalid room type, return -1 to indicate error.
#
# 2. Write calculate_room_cost(room_price, nights, is_holiday=False):
#    - Base room cost = room_price * nights.
#    - If holiday season (is_holiday=True): Add 25% surcharge (multiply by 1.25).
#    - Return total room cost.
#
# 3. Write calculate_service_cost(guests_count, buffet_meals=0, airport_pickup=False, laundry=False):
#    - Breakfast Buffet: 120,000 VND / guest / meal. (Cost = guests_count * buffet_meals * 120000)
#    - Airport pickup: 350,000 VND flat fee (if airport_pickup=True).
#    - Laundry package: 150,000 VND flat fee (if laundry=True).
#    - Return total extra service cost.
#
# 4. Write calculate_membership_discount(subtotal, membership_tier="STANDARD"):
#    - Loyalty tiers:
#      + "SILVER": 5% discount on subtotal.
#      + "GOLD": 10% discount on subtotal.
#      + "PLATINUM": 15% discount on subtotal.
#      + "STANDARD" or other: No discount (0 VND).
#    - Return discount amount.
#
# 5. Write main():
#    - Input customer info: Name, Room type, Nights, Guests count.
#    - Validate room type; display error and exit if invalid.
#    - Ask if it's holiday season (y/n).
#    - Ask for add-on services: buffet meals count, airport pickup (y/n), laundry (y/n).
#    - Input membership tier.
#    - Apply 8% VAT tax and print a detailed hotel invoice.

# ==============================================================================
# [STARTER CODE]
# ==============================================================================

def get_room_price(room_type):
    # Trả về giá phòng tương ứng hoặc -1 nếu không hợp lệ
    # Return room price or -1 if invalid
    pass

def calculate_room_cost(room_price, nights, is_holiday=False):
    # Tính tiền phòng có tính phụ thu ngày lễ nếu có
    # Calculate room cost with holiday surcharge if applicable
    pass

def calculate_service_cost(guests_count, buffet_meals=0, airport_pickup=False, laundry=False):
    # Tính tổng chi phí các dịch vụ kèm theo
    # Calculate total add-on services cost
    pass

def calculate_membership_discount(subtotal, membership_tier="STANDARD"):
    # Tính số tiền chiết khấu theo hạng thẻ thành viên
    # Calculate membership discount amount
    pass

def print_hotel_invoice(guest_name, room_type, nights, room_cost, service_cost, discount, vat, final_total):
    # In hóa đơn thanh toán khách sạn
    # Print formatted hotel invoice
    pass

def main():
    # Nhập thông tin, gọi các hàm và xuất hóa đơn
    # Input details, execute functions and display receipt
    pass

if __name__ == "__main__":
    main()
