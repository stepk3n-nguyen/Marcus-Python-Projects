# ==============================================================================
# PROJECT 5: TÍNH LƯƠNG & THUẾ THU NHẬP DOANH NGHIỆP / PAYROLL & TAX CALCULATOR
# LỜI GIẢI HOÀN CHỈNH / FULL SOLUTION
# ==============================================================================

def calculate_base_salary(basic_salary, actual_workdays, standard_workdays=22):
    """Calculate base salary from actual workdays."""
    daily_wage = basic_salary / standard_workdays
    base_salary = daily_wage * actual_workdays
    return round(base_salary, 2)

def calculate_overtime_pay(ot_hours, hourly_rate=50000, ot_multiplier=1.5):
    """Calculate overtime pay."""
    ot_pay = ot_hours * hourly_rate * ot_multiplier
    return round(ot_pay, 2)

def calculate_kpi_bonus(basic_salary, rank):
    """Calculate KPI performance bonus based on grade A/B/C/D."""
    rank = rank.upper().strip()
    if rank == "A":
        rate = 0.30
    elif rank == "B":
        rate = 0.15
    elif rank == "C":
        rate = 0.05
    else:
        rate = 0.0
    
    return round(basic_salary * rate, 2)

def calculate_insurance(insurance_salary):
    """Calculate 10.5% mandatory social & health insurance."""
    return round(insurance_salary * 0.105, 2)

def calculate_income_tax(total_income, dependents=0):
    """Calculate progressive personal income tax."""
    personal_deduction = 11000000
    dependent_deduction = dependents * 4400000
    
    taxable_income = total_income - personal_deduction - dependent_deduction
    
    if taxable_income <= 0:
        return 0.0
    
    tax = 0.0
    if taxable_income <= 5000000:
        tax = taxable_income * 0.05
    elif taxable_income <= 10000000:
        tax = (5000000 * 0.05) + (taxable_income - 5000000) * 0.10
    elif taxable_income <= 18000000:
        tax = (5000000 * 0.05) + (5000000 * 0.10) + (taxable_income - 10000000) * 0.15
    else:
        tax = (5000000 * 0.05) + (5000000 * 0.10) + (8000000 * 0.15) + (taxable_income - 18000000) * 0.20
        
    return round(tax, 2)

def print_payslip(name, base_salary, ot_pay, kpi_bonus, insurance, tax, net_salary):
    """Print formatted payslip summary."""
    print("\n" + "=" * 52)
    print(f"{'EMPLOYEE PAYSLIP / PHIẾU LƯƠNG':^52}")
    print("=" * 52)
    print(f" Employee / Nhân viên: {name}")
    print("-" * 52)
    print(f" [+] Base Salary / Lương chính:   {base_salary:>15,.0f} VND")
    print(f" [+] Overtime Pay / Tiền OT:       {ot_pay:>15,.0f} VND")
    print(f" [+] KPI Bonus / Thưởng KPI:       {kpi_bonus:>15,.0f} VND")
    total_income = base_salary + ot_pay + kpi_bonus
    print(f"  -> Total Income / Tổng thu nhập: {total_income:>15,.0f} VND")
    print("-" * 52)
    print(f" [-] Insurance (10.5%) / Bảo hiểm: {insurance:>15,.0f} VND")
    print(f" [-] Income Tax / Thuế TNCN:       {tax:>15,.0f} VND")
    print("=" * 52)
    print(f" [★] NET SALARY / THỰC LĨNH:       {net_salary:>15,.0f} VND")
    print("=" * 52 + "\n")

def main():
    print("=== EMPLOYEE PAYROLL & TAX CALCULATOR ===")
    
    name = input("Enter employee name / Nhập họ tên: ")
    basic_salary = float(input("Enter basic salary / Lương cơ bản (VND): "))
    actual_workdays = float(input("Enter actual workdays / Số ngày làm (chuẩn 22): "))
    ot_hours = float(input("Enter OT hours / Số giờ OT: "))
    rank = input("Enter KPI rank / Xếp loại KPI (A/B/C/D): ")
    dependents = int(input("Enter dependents / Số người phụ thuộc: "))
    
    # 1. Income calculations
    base_salary = calculate_base_salary(basic_salary, actual_workdays)
    ot_rate = basic_salary / (22 * 8)
    ot_pay = calculate_overtime_pay(ot_hours, hourly_rate=ot_rate, ot_multiplier=1.5)
    kpi_bonus = calculate_kpi_bonus(basic_salary, rank)
    total_income = base_salary + ot_pay + kpi_bonus
    
    # 2. Deductions
    insurance = calculate_insurance(basic_salary)
    tax = calculate_income_tax(total_income, dependents)
    
    # 3. Net Salary
    net_salary = total_income - insurance - tax
    
    # 4. Output
    print_payslip(name, base_salary, ot_pay, kpi_bonus, insurance, tax, net_salary)

if __name__ == "__main__":
    main()
