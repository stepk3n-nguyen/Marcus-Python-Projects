# ==============================================================================
# PROJECT 2: MÁY RÚT TIỀN ATM MINI / MINI ATM BANKING MACHINE
# LỜI GIẢI HOÀN CHỈNH / FULL SOLUTION
# ==============================================================================

# 1. Hàm xác thực mã PIN người dùng
# 1. Function to authenticate user PIN
def pin_valid(pin_correct, max_attempts=3):
    print("=== ATM LOGIN ===")
    
    # Dùng vòng lặp for để giới hạn số lần nhập
    # Use a for loop to limit number of attempts
    for lan_thu in range(1, max_attempts + 1):
        pin_input = input(f"Enter PIN (Attempt {lan_thu}/{max_attempts}): ")
        
        # So sánh mã PIN nhập vào với mã PIN chuẩn
        # Compare entered PIN with correct PIN
        if pin_input == pin_correct:
            print("Login successful!")
            return True
        else:
            remaining_attempts = max_attempts - lan_thu
            if remaining_attempts > 0:
                print(f"Wrong PIN! You have {remaining_attempts} attempt(s) left.")
            else:
                print("Too many failed attempts! Your card is locked.")
                return False


# 2. Hàm kiểm tra và hiển thị số dư
# 2. Function to check and display balance
def check_balance(balance):
    print(f"Current account balance: {balance} VND")


# 3. Hàm nạp tiền vào tài khoản
# 3. Function to deposit money into account
def deposit(balance, deposit_amount):
    # Kiểm tra số tiền nạp phải lớn hơn 0
    # Check if deposit amount is greater than 0
    if deposit_amount > 0:
        # Dùng toán tử cộng để cập nhật số dư
        # Use addition operator to update balance
        new_balance = balance + deposit_amount
        print(f"Successfully deposited {deposit_amount} VND.")
        return new_balance
    else:
        print("Deposit amount must be greater than 0!")
        return balance


# 4. Hàm rút tiền từ tài khoản
# 4. Function to withdraw money from account
def withdraw(balance, withdraw_amount):
    # Điều kiện 1: Số tiền rút phải lớn hơn 0
    # Condition 1: Withdrawal amount must be greater than 0
    if withdraw_amount <= 0:
        print("Withdrawal amount must be greater than 0!")
        return balance

    # Điều kiện 2: Số tiền rút phải chia hết cho 50000 (toán tử %)
    # Condition 2: Withdrawal amount must be divisible by 50000 (% operator)
    elif withdraw_amount % 50000 != 0:
        print("Withdrawal amount must be a multiple of 50,000 VND!")
        return balance

    # Điều kiện 3: Số tiền rút phải nhỏ hơn hoặc bằng số dư hiện có
    # Condition 3: Withdrawal amount must be less than or equal to balance
    elif withdraw_amount > balance:
        print("Insufficient balance to perform this transaction!")
        return balance

    # Thực hiện trừ tiền khi thỏa mãn mọi điều kiện
    # Deduct money when all conditions are met
    else:
        new_balance = balance - withdraw_amount
        print(f"Successfully withdrew {withdraw_amount} VND. Please take your cash!")
        return new_balance


# 5. Hàm chính điều khiển menu ATM
# 5. Main function to control ATM menu
def main():
    balance = 1000000  # Khởi tạo số dư ban đầu 1 triệu đồng / Initial balance
    pin_correct = "1234"

    # Bước 1: Gọi hàm xác thực mã PIN
    # Step 1: Call PIN authentication function
    da_dang_nhap = pin_valid(pin_correct, 3)

    # Nếu không đăng nhập được thì kết thúc chương trình
    # If login fails then terminate program
    if not da_dang_nhap:
        return

    # Bước 2: Dùng vòng lặp while True tạo menu tương tác
    # Step 2: Use while True loop to create interactive menu
    while True:
        print("\n" + "=" * 40)
        print("--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("0. Exit")
        print("=" * 40)

        lua_chon = input("Choose option (0-3): ")

        # Xử lý các lựa chọn bằng cấu trúc if - elif - else
        # Handle choices using if - elif - else structure
        if lua_chon == "1":
            check_balance(balance)
        elif lua_chon == "2":
            deposit_amount = float(input("Enter amount to deposit: "))
            balance = deposit(balance, deposit_amount)
        elif lua_chon == "3":
            withdraw_amount = float(input("Enter amount to withdraw: "))
            balance = withdraw(balance, withdraw_amount)
        elif lua_chon == "0":
            print("Thank you for using ATM services. Goodbye!")
            break  # Thoát khỏi vòng lặp / Exit loop
        else:
            print("Invalid option! Please choose between 0 and 3.")


if __name__ == "__main__":
    main()
