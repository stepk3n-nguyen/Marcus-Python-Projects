# ==============================================================================
# PROJECT 7: TÍNH LÃI SUẤT TIẾT KIỆM & LỊCH TRẢ GÓP NGÂN HÀNG / BANK FINANCIAL PLANNER
# ==============================================================================

# ------------------------------------------------------------------------------
# [TIẾNG VIỆT] ĐỀ BÀI: HOẠCH ĐỊNH TIẾT KIỆM & VAY TRẢ GÓP NGÂN HÀNG
# ------------------------------------------------------------------------------
# MỤC TIÊU:
# Nâng cao tư duy xây dựng hàm và xử lý công thức toán học/tài chính trong lập trình:
# - Hàm trả về nhiều giá trị (Return multiple values / Tuple).
# - Vận dụng công thức toán học phức tạp (Lũy thừa, Lãi kép, Niên kim cố định EMI).
# - Xây dựng hệ thống menu đa chức năng lồng các hàm điều phối.
#
# YÊU CẦU:
# 1. Viết hàm calculate_savings_interest(deposit_amount, months, interest_type="SIMPLE"):
#    - Bảng lãi suất năm theo kỳ hạn:
#      + Dưới 6 tháng: 4.5% / năm
#      + Từ 6 đến dưới 12 tháng: 5.5% / năm
#      + Từ 12 tháng trở lên: 6.8% / năm
#    - Lãi đơn (interest_type == "SIMPLE"):
#      + interest = deposit_amount * (annual_rate / 100) * (months / 12)
#      + total_payout = deposit_amount + interest
#    - Lãi kép hàng tháng (interest_type == "COMPOUND"):
#      + total_payout = deposit_amount * (1 + (annual_rate / 100) / 12) ** months
#      + interest = total_payout - deposit_amount
#    - Trả về 2 giá trị (tuple): (interest, total_payout).
#
# 2. Viết hàm check_loan_eligibility(monthly_income, monthly_payment, has_bad_debt=False):
#    - Nếu has_bad_debt == True -> Từ chối vay (False, "Lý do: Khách hàng có lịch sử nợ xấu").
#    - Tỷ lệ trả nợ trên thu nhập (DTI - Debt-to-Income):
#      + dti_ratio = monthly_payment / monthly_income
#      + Nếu dti_ratio <= 0.60 (khoản trả góp <= 60% thu nhập): Đủ điều kiện (True, "Đủ điều kiện vay vốn")
#      + Nếu dti_ratio > 0.60: Không đủ điều kiện (False, "Lý do: Khoản trả hàng tháng vượt quá 60% thu nhập").
#    - Trả về tuple: (is_approved, message).
#
# 3. Viết hàm calculate_loan_emi(loan_amount, annual_rate, months):
#    - Tính số tiền cố định phải trả đều mỗi tháng (công thức EMI chuẩn ngân hàng):
#      + r = (annual_rate / 100) / 12 (lãi suất theo tháng)
#      + EMI = loan_amount * [r * (1 + r)^months] / [(1 + r)^months - 1]
#    - Tổng tiền phải trả = EMI * months.
#    - Tổng tiền lãi phải trả = Tổng tiền phải trả - loan_amount.
#    - Trả về 3 giá trị: (monthly_emi, total_payment, total_interest).
#
# 4. Viết hàm print_loan_schedule(loan_amount, monthly_emi, total_payment, total_interest, months):
#    - In bảng kế hoạch tài chính trả góp rõ ràng, định dạng tiền tệ.
#
# 5. Viết hàm main():
#    - Hiển thị menu cho người dùng chọn:
#      1. Tính tiền gửi tiết kiệm (Lãi đơn / Lãi kép).
#      2. Thẩm định điều kiện vay & Tính lịch trả góp hàng tháng.
#      3. Thoát chương trình.
#    - Dùng vòng lặp while để duy trì chương trình.

# ------------------------------------------------------------------------------
# [ENGLISH] EXERCISE: BANK SAVINGS & LOAN REPAYMENT PLANNER
# ------------------------------------------------------------------------------
# GOALS:
# Advanced function & mathematical logic practice:
# - Functions returning multiple values (Tuples).
# - Complex mathematical formulas (Exponents, Compound interest, Equated Monthly Installment EMI).
# - Multi-option interactive menu architecture.
#
# REQUIREMENTS:
# 1. Write calculate_savings_interest(deposit_amount, months, interest_type="SIMPLE"):
#    - Annual interest rate tiers:
#      + Under 6 months: 4.5% / year
#      + 6 to 11 months: 5.5% / year
#      + 12 months or more: 6.8% / year
#    - Simple Interest (interest_type == "SIMPLE"):
#      + interest = deposit_amount * (annual_rate / 100) * (months / 12)
#      + total_payout = deposit_amount + interest
#    - Monthly Compound Interest (interest_type == "COMPOUND"):
#      + total_payout = deposit_amount * (1 + (annual_rate / 100) / 12) ** months
#      + interest = total_payout - deposit_amount
#    - Return 2 values: (interest, total_payout).
#
# 2. Write check_loan_eligibility(monthly_income, monthly_payment, has_bad_debt=False):
#    - If has_bad_debt == True -> Reject loan (False, "Rejected: Bad credit history detected").
#    - Debt-to-Income (DTI) ratio:
#      + dti_ratio = monthly_payment / monthly_income
#      + If dti_ratio <= 0.60: Approve loan (True, "Loan approved: DTI <= 60%")
#      + If dti_ratio > 0.60: Reject loan (False, "Rejected: Monthly payment exceeds 60% income").
#    - Return tuple: (is_approved, message).
#
# 3. Write calculate_loan_emi(loan_amount, annual_rate, months):
#    - Calculate standard monthly fixed payment (EMI formula):
#      + r = (annual_rate / 100) / 12 (monthly rate)
#      + EMI = loan_amount * [r * (1 + r)^months] / [(1 + r)^months - 1]
#    - Total payment = EMI * months.
#    - Total interest = Total payment - loan_amount.
#    - Return 3 values: (monthly_emi, total_payment, total_interest).
#
# 4. Write print_loan_schedule(loan_amount, monthly_emi, total_payment, total_interest, months):
#    - Print a formatted loan repayment schedule summary.
#
# 5. Write main():
#    - Display interactive menu:
#      1. Calculate savings return (Simple / Compound).
#      2. Loan eligibility check & EMI repayment schedule.
#      3. Exit.
#    - Use a while loop to keep the program active.

# ==============================================================================
# [STARTER CODE]
# ==============================================================================

def calculate_savings_interest(deposit_amount, months, interest_type="SIMPLE"):
    # Tính tiền lãi và tổng tiền nhận được theo kỳ hạn và loại lãi
    # Calculate interest and total payout based on term and interest type
    pass

def check_loan_eligibility(monthly_income, monthly_payment, has_bad_debt=False):
    # Thẩm định hồ sơ vay dựa trên nợ xấu và tỷ lệ DTI
    # Evaluate loan eligibility based on bad debt and DTI ratio
    pass

def calculate_loan_emi(loan_amount, annual_rate, months):
    # Tính tiền trả góp cố định hàng tháng theo công thức EMI
    # Calculate fixed monthly EMI repayment
    pass

def print_loan_schedule(loan_amount, monthly_emi, total_payment, total_interest, months):
    # In bảng kế hoạch trả nợ
    # Print formatted loan repayment schedule
    pass

def main():
    # Xây dựng menu lựa chọn và điều phối các hàm
    # Build menu loop and coordinate functions
    pass

if __name__ == "__main__":
    main()
