# ==============================================================================
# PROJECT 6: QUẢN LÝ ĐẶT PHÒNG & DỊCH VỤ KHÁCH SẠN / HOTEL BOOKING MANAGER
# LỜI GIẢI HOÀN CHỈNH / FULL SOLUTION
# ==============================================================================

def get_room_price(room_type):
    """Get nightly room rate. Returns -1 if invalid."""
    room_type = room_type.upper().strip()
    price_table = {
        "STANDARD": 500000,
        "DELUXE": 900000,
        "SUITE": 1600000,
        "VIP": 2500000
    }
    return price_table.get(room_type, -1)

def calculate_room_cost(room_price, nights, is_holiday=False):
    """Calculate base room cost with optional holiday surcharge."""
    base_cost = room_price * nights
    if is_holiday:
        return round(base_cost * 1.25, 2)
    return round(base_cost, 2)

def calculate_service_cost(guests_count, buffet_meals=0, airport_pickup=False, laundry=False):
    """Calculate total add-on service cost."""
    buffet_rate = 120000
    pickup_rate = 350000
    laundry_rate = 150000
    
    buffet_cost = guests_count * buffet_meals * buffet_rate
    pickup_cost = pickup_rate if airport_pickup else 0
    laundry_cost = laundry_rate if laundry else 0
    
    return buffet_cost + pickup_cost + laundry_cost

def calculate_membership_discount(subtotal, membership_tier="STANDARD"):
    """Calculate loyalty membership discount."""
    membership_tier = membership_tier.upper().strip()
    if membership_tier == "PLATINUM":
        rate = 0.15
    elif membership_tier == "GOLD":
        rate = 0.10
    elif membership_tier == "SILVER":
        rate = 0.05
    else:
        rate = 0.0
        
    return round(subtotal * rate, 2)

def print_hotel_invoice(guest_name, room_type, nights, room_cost, service_cost, discount, vat, final_total):
    """Print formatted hotel invoice."""
    print("\n" + "=" * 55)
    print(f"{'HOTEL BOOKING INVOICE / HÓA ĐƠN KHÁCH SẠN':^55}")
    print("=" * 55)
    print(f" Guest / Khách hàng: {guest_name}")
    print(f" Room / Loại phòng:  {room_type.upper()} ({nights} nights / đêm)")
    print("-" * 55)
    print(f" [+] Room Cost / Tiền phòng:      {room_cost:>15,.0f} VND")
    print(f" [+] Services / Dịch vụ kèm theo: {service_cost:>15,.0f} VND")
    print(f" [-] Loyalty Discount / Giảm giá: {discount:>15,.0f} VND")
    print(f" [+] VAT Tax (8%) / Thuế VAT:     {vat:>15,.0f} VND")
    print("=" * 55)
    print(f" [★] FINAL TOTAL / TỔNG THANH TOÁN:{final_total:>15,.0f} VND")
    print("=" * 55 + "\n")

def main():
    print("=== HOTEL BOOKING & SERVICE MANAGER ===")
    
    guest_name = input("Enter guest name / Nhập tên khách: ")
    room_type = input("Choose room type / Loại phòng (STANDARD / DELUXE / SUITE / VIP): ")
    
    room_price = get_room_price(room_type)
    if room_price == -1:
        print("❌ Error: Invalid room type! / Loại phòng không tồn tại!")
        return
    
    nights = int(input("Enter number of nights / Số đêm ở: "))
    guests_count = int(input("Enter number of guests / Số khách: "))
    
    holiday_input = input("Is it a holiday? / Dịp lễ không? (y/n): ").strip().lower()
    is_holiday = (holiday_input == "y" or holiday_input == "yes")
    
    print("\n--- Add-on Services / Dịch vụ bổ sung ---")
    buffet_meals = int(input("Breakfast buffet count / Số bữa buffet: "))
    pickup_input = input("Airport pickup / Đón sân bay? (y/n): ").strip().lower()
    airport_pickup = (pickup_input == "y" or pickup_input == "yes")
    
    laundry_input = input("Laundry package / Giặt ủi? (y/n): ").strip().lower()
    laundry = (laundry_input == "y" or laundry_input == "yes")
    
    membership_tier = input("Membership tier / Hạng thẻ (STANDARD / SILVER / GOLD / PLATINUM): ")
    
    # Calculations
    room_cost = calculate_room_cost(room_price, nights, is_holiday)
    service_cost = calculate_service_cost(guests_count, buffet_meals, airport_pickup, laundry)
    subtotal = room_cost + service_cost
    
    discount = calculate_membership_discount(subtotal, membership_tier)
    after_discount = subtotal - discount
    
    vat = round(after_discount * 0.08, 2)
    final_total = after_discount + vat
    
    print_hotel_invoice(guest_name, room_type, nights, room_cost, service_cost, discount, vat, final_total)

if __name__ == "__main__":
    main()
