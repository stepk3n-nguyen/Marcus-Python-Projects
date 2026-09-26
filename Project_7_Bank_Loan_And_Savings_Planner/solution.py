# ==============================================================================
# PROJECT 7: TÍNH LÃI SUẤT TIẾT KIỆM & LỊCH TRẢ GÓP NGÂN HÀNG / BANK FINANCIAL PLANNER
# LỜI GIẢI HOÀN CHỈNH / FULL SOLUTION
# ==============================================================================

def calculate_savings_interest(deposit_amount, months, interest_type="SIMPLE"):
    """
    Calculate savings interest return (Simple or Monthly Compounded).
    Returns: (interest, total_payout)
    """
    if months < 6:
        annual_rate = 4.5
    elif months < 12:
        annual_rate = 5.5
    else:
        annual_rate = 6.8

    r = annual_rate / 100

    interest_type = interest_type.upper().strip()
    if interest_type == "COMPOUND":
        total_payout = deposit_amount * ((1 + r / 12) ** months)
        interest = total_payout - deposit_amount
    else:
        interest = deposit_amount * r * (months / 12)
        total_payout = deposit_amount + interest

    return round(interest, 2), round(total_payout, 2)

def check_loan_eligibility(monthly_income, monthly_payment, has_bad_debt=False):
    """
    Check loan approval eligibility based on credit history and DTI ratio.
    Returns: (is_approved: bool, message: str)
    """
    if has_bad_debt:
        return False, "Loan rejected: Bad credit record found on CIC / Từ chối do có nợ xấu."

    if monthly_income <= 0:
        return False, "Invalid monthly income / Thu nhập không hợp lệ."

    dti_ratio = monthly_payment / monthly_income
    if dti_ratio <= 0.60:
        return True, f"Loan approved! DTI ratio: {dti_ratio*100:.1f}% <= 60% / Đủ điều kiện duyệt vay."
    else:
        return False, f"Loan rejected: DTI ratio ({dti_ratio*100:.1f}%) exceeds safety limit 60% / Khoản trả vượt 60% thu nhập."

def calculate_loan_emi(loan_amount, annual_rate, months):
    """
    Calculate fixed Equated Monthly Installment (EMI).
    Returns: (monthly_emi, total_payment, total_interest)
    """
    r_month = (annual_rate / 100) / 12

    if r_month == 0:
        emi = loan_amount / months
    else:
        factor = (1 + r_month) ** months
        emi = loan_amount * (r_month * factor) / (factor - 1)

    total_payment = emi * months
    total_interest = total_payment - loan_amount

    return round(emi, 2), round(total_payment, 2), round(total_interest, 2)

def print_loan_schedule(loan_amount, monthly_emi, total_payment, total_interest, months):
    """Print formatted loan schedule."""
    print("\n" + "=" * 55)
    print(f"{'LOAN REPAYMENT SCHEDULE / KẾ HOẠCH TRẢ GÓP (EMI)':^55}")
    print("=" * 55)
    print(f" Principal Loan / Tiền vay gốc: {loan_amount:>15,.0f} VND")
    print(f" Term / Kỳ hạn vay:              {months:>15} months / tháng")
    print("-" * 55)
    print(f" [★] Monthly EMI / Trả mỗi tháng:{monthly_emi:>15,.0f} VND")
    print(f" [+] Total Interest / Tổng lãi:  {total_interest:>15,.0f} VND")
    print(f" [=] Total Payout / Tổng gốc+lãi:{total_payment:>15,.0f} VND")
    print("=" * 55 + "\n")

def main():
    while True:
        print("\n" + "=" * 52)
        print("   BANK FINANCIAL PLANNER / HOẠCH ĐỊNH TÀI CHÍNH")
        print("=" * 52)
        print(" 1. Calculate Savings Interest / Tính lãi tiết kiệm")
        print(" 2. Loan Approval & EMI Schedule / Tính vay trả góp")
        print(" 3. Exit / Thoát")
        print("-" * 52)
        choice = input("Select an option / Chọn chức năng (1-3): ").strip()

        if choice == "1":
            print("\n--- SAVINGS INTEREST CALCULATOR ---")
            deposit = float(input("Enter deposit amount / Tiền gửi (VND): "))
            months = int(input("Enter term in months / Kỳ hạn (tháng): "))
            interest_type = input("Interest type (SIMPLE: Lãi đơn / COMPOUND: Lãi kép): ")

            interest, total = calculate_savings_interest(deposit, months, interest_type)
            print("-" * 48)
            print(f" Interest earned / Tiền lãi:   {interest:>15,.0f} VND")
            print(f" Total payout / Tổng rút về:    {total:>15,.0f} VND")
            print("-" * 48)

        elif choice == "2":
            print("\n--- LOAN APPRAISAL & EMI CALCULATOR ---")
            income = float(input("Enter monthly net income / Thu nhập tháng (VND): "))
            loan_amount = float(input("Enter desired loan / Số tiền vay (VND): "))
            rate = float(input("Enter annual interest rate / Lãi suất năm (%): "))
            months = int(input("Enter loan term / Số tháng vay: "))
            
            bad_debt_input = input("Any bad credit history? / Có nợ xấu không? (y/n): ").strip().lower()
            has_bad_debt = (bad_debt_input == "y" or bad_debt_input == "yes")

            emi, total_pay, total_int = calculate_loan_emi(loan_amount, rate, months)
            is_approved, msg = check_loan_eligibility(income, emi, has_bad_debt)

            print("\n" + ">" * 15 + " APPRAISAL RESULT " + "<" * 15)
            if is_approved:
                print(f"✅ {msg}")
                print_loan_schedule(loan_amount, emi, total_pay, total_int, months)
            else:
                print(f"❌ {msg}")
                print(f"   (Monthly EMI is {emi:,.0f} VND/month compared to income {income:,.0f} VND)")

        elif choice == "3":
            print("Thank you for using our financial services. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
