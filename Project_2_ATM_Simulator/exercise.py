# ==============================================================================
# PROJECT 2: MÁY RÚT TIỀN ATM MINI / MINI ATM BANKING MACHINE
# ==============================================================================

# ------------------------------------------------------------------------------
# [TIẾNG VIỆT] ĐỀ BÀI: MÁY RÚT TIỀN ATM MINI
# ------------------------------------------------------------------------------
# MỤC TIÊU:
# Luyện tập: Hàm (function), Cấu trúc rẽ nhánh (if - elif - else), Vòng lặp (while/for), Toán tử chia lấy dư (%).
#
# YÊU CẦU:
# 1. Viết hàm pin_valid(pin_correct, max_attempts) cho phép người dùng nhập mã PIN tối đa 3 lần.
# 2. Nếu nhập đúng PIN thì trả về True, nếu sai quá 3 lần thì in thông báo khóa thẻ và trả về False.
# 3. Viết hàm check_balance(balance) in ra số dư tài khoản hiện tại.
# 4. Viết hàm deposit(balance, deposit_amount) nhận vào số tiền muốn nạp (phải > 0), cộng vào số dư và trả về số dư mới.
# 5. Viết hàm withdraw(balance, withdraw_amount) kiểm tra các điều kiện:
#    - Số tiền rút phải lớn hơn 0 (withdraw_amount > 0).
#    - Số tiền rút phải là bội số của 50000 (withdraw_amount % 50000 == 0).
#    - Số tiền rút không được vượt quá số dư hiện có (withdraw_amount <= balance).
#    - Trừ tiền và trả về số dư mới nếu hợp lệ, ngược lại in thông báo lỗi và giữ nguyên số dư.
# 6. Dùng vòng lặp while True tạo menu gồm các lựa chọn (1: Xem số dư, 2: Nạp tiền, 3: Rút tiền, 0: Thoát).

# ------------------------------------------------------------------------------
# [ENGLISH] EXERCISE: MINI ATM BANKING MACHINE
# ------------------------------------------------------------------------------
# GOALS:
# Practice: Functions, Conditional statements (if - elif - else), Loops (while/for), Modulo operator (%).
#
# REQUIREMENTS:
# 1. Write a function pin_valid(pin_correct, max_attempts) allowing the user to enter PIN up to 3 times.
# 2. If the PIN is correct return True, if wrong more than 3 times print card locked message and return False.
# 3. Write a function check_balance(balance) to print the current account balance.
# 4. Write a function deposit(balance, deposit_amount) taking deposit amount (> 0), adding to balance and returning new balance.
# 5. Write a function withdraw(balance, withdraw_amount) checking the following conditions:
#    - Withdrawal amount must be greater than 0 (withdraw_amount > 0).
#    - Withdrawal amount must be a multiple of 50000 (withdraw_amount % 50000 == 0).
#    - Withdrawal amount must not exceed current balance (withdraw_amount <= balance).
#    - Deduct money and return new balance if valid, otherwise print error message and keep balance unchanged.
# 6. Use a while True loop to create a menu with options (1: Check Balance, 2: Deposit, 3: Withdraw, 0: Exit).


# ==============================================================================
# [KHUNG BÀI TẬP / STARTER CODE]
# ==============================================================================

def pin_valid(pin_correct, max_attempts=3):
    # Dùng vòng lặp for hoặc while để đếm số lần nhập PIN
    # Use for or while loop to count PIN entry attempts
    pass

def check_balance(balance):
    # In số dư hiện tại
    # Print current balance
    pass

def deposit(balance, deposit_amount):
    # Kiểm tra điều kiện nạp và cộng tiền vào số dư
    # Check deposit condition and add amount to balance
    pass

def withdraw(balance, withdraw_amount):
    # Kiểm tra các điều kiện rút tiền và trừ tiền
    # Check withdrawal conditions and deduct amount
    pass

def main():
    balance = 1000000  # Số dư khởi tạo 1 triệu đồng / Initial balance: 1,000,000 VND
    pin_correct = "1234"
    
    # 1. Xác thực người dùng
    # 1. Authenticate user
    
    # 2. Vòng lặp menu ATM
    # 2. ATM menu loop
    pass

if __name__ == "__main__":
    main()
