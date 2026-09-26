# ==============================================================================
# PROJECT 5: TÍNH LƯƠNG & THUẾ THU NHẬP DOANH NGHIỆP / PAYROLL & TAX CALCULATOR
# ==============================================================================

# ------------------------------------------------------------------------------
# [TIẾNG VIỆT] ĐỀ BÀI: HỆ THỐNG TÍNH LƯƠNG & THUẾ TNCN
# ------------------------------------------------------------------------------
# MỤC TIÊU:
# Luyện tập nâng cao:
# - Hàm có tham số mặc định (Default arguments).
# - Hàm gọi lồng nhau (Function calling function).
# - Xử lý tính toán lũy tiến theo từng bậc (Progressive tax calculation).
# - Tách nhỏ bài toán lớn thành các hàm độc lập.
#
# YÊU CẦU:
# 1. Viết hàm calculate_base_salary(basic_salary, actual_workdays, standard_workdays=22):
#    - Lương ngày = basic_salary / standard_workdays.
#    - Lương chính = Lương ngày * actual_workdays.
#    - Trả về số tiền lương chính (làm tròn 2 chữ số).
#
# 2. Viết hàm calculate_overtime_pay(ot_hours, hourly_rate=50000, ot_multiplier=1.5):
#    - Tiền OT = ot_hours * hourly_rate * ot_multiplier.
#    - Trả về tiền làm thêm giờ.
#
# 3. Viết hàm calculate_kpi_bonus(basic_salary, rank):
#    - Dựa vào xếp loại KPI (A, B, C, D):
#      + "A": Thưởng 30% lương cơ bản (0.30)
#      + "B": Thưởng 15% lương cơ bản (0.15)
#      + "C": Thưởng 5% lương cơ bản (0.05)
#      + "D" hoặc khác: Không có thưởng (0)
#    - Trả về tiền thưởng KPI.
#
# 4. Viết hàm calculate_insurance(insurance_salary):
#    - Người lao động đóng: 8% BHXH, 1.5% BHYT, 1% BHTN (Tổng = 10.5%).
#    - Trả về số tiền bảo hiểm khấu trừ = insurance_salary * 0.105.
#
# 5. Viết hàm calculate_income_tax(total_income, dependents=0):
#    - Giảm trừ gia cảnh bản thân: 11,000,000 VND.
#    - Giảm trừ người phụ thuộc: 4,400,000 VND / người.
#    - Thu nhập chịu thuế (TNCT) = total_income - 11,000,000 - (dependents * 4,400,000).
#    - Nếu TNCT <= 0: Thuế = 0.
#    - Nếu TNCT > 0, tính theo biểu thuế lũy tiến từng phần:
#      + Bậc 1: Đến 5,000,000 VND -> 5%
#      + Bậc 2: Trên 5,000,000 đến 10,000,000 VND -> 10%
#      + Bậc 3: Trên 10,000,000 đến 18,000,000 VND -> 15%
#      + Bậc 4: Trên 18,000,000 VND -> 20%
#    - Trả về số tiền thuế TNCN phải nộp.
#
# 6. Viết hàm main():
#    - Nhập thông tin nhân viên: Tên, Lương cơ bản, Số ngày làm việc, Giờ OT, Xếp loại KPI, Số người phụ thuộc.
#    - Gọi các hàm trên để tính lương thực nhận (Net):
#      Net = Lương chính + OT + Thưởng KPI - Bảo hiểm - Thuế TNCN
#    - In phiếu lương (Payslip) chi tiết.

# ------------------------------------------------------------------------------
# [ENGLISH] EXERCISE: PAYROLL & PERSONAL INCOME TAX CALCULATOR
# ------------------------------------------------------------------------------
# GOALS:
# Advanced practice:
# - Functions with default arguments.
# - Functions calling other functions.
# - Progressive bracket calculations (Personal income tax).
# - Modularizing large tasks into clean, reusable functions.
#
# REQUIREMENTS:
# 1. Write calculate_base_salary(basic_salary, actual_workdays, standard_workdays=22):
#    - Daily wage = basic_salary / standard_workdays.
#    - Base pay = Daily wage * actual_workdays.
#    - Return base pay rounded to 2 decimal places.
#
# 2. Write calculate_overtime_pay(ot_hours, hourly_rate=50000, ot_multiplier=1.5):
#    - OT pay = ot_hours * hourly_rate * ot_multiplier.
#    - Return total OT pay.
#
# 3. Write calculate_kpi_bonus(basic_salary, rank):
#    - Based on KPI rating (A, B, C, D):
#      + "A": Bonus 30% of basic salary (0.30)
#      + "B": Bonus 15% of basic salary (0.15)
#      + "C": Bonus 5% of basic salary (0.05)
#      + "D" or others: No bonus (0)
#    - Return KPI bonus amount.
#
# 4. Write calculate_insurance(insurance_salary):
#    - Deductions: 8% Social, 1.5% Health, 1% Unemployment (Total = 10.5%).
#    - Return insurance deduction = insurance_salary * 0.105.
#
# 5. Write calculate_income_tax(total_income, dependents=0):
#    - Personal deduction: 11,000,000 VND.
#    - Dependent deduction: 4,400,000 VND per dependent.
#    - Taxable income = total_income - 11,000,000 - (dependents * 4,400,000).
#    - If taxable income <= 0: Tax = 0.
#    - If taxable income > 0, calculate progressive tax brackets:
#      + Tier 1: Up to 5,000,000 VND -> 5%
#      + Tier 2: 5,000,001 to 10,000,000 VND -> 10%
#      + Tier 3: 10,000,001 to 18,000,000 VND -> 15%
#      + Tier 4: Over 18,000,000 VND -> 20%
#    - Return personal income tax amount.
#
# 6. Write main():
#    - Input employee info: Name, Basic salary, Workdays, OT hours, KPI rank, Dependents count.
#    - Call above functions to compute Net Salary:
#      Net = Base pay + OT + KPI Bonus - Insurance - Tax
#    - Print a formatted payslip summary.

# ==============================================================================
# [STARTER CODE]
# ==============================================================================

def calculate_base_salary(basic_salary, actual_workdays, standard_workdays=22):
    # Tính lương chính theo số ngày công thực tế
    # Calculate base salary based on actual workdays
    pass

def calculate_overtime_pay(ot_hours, hourly_rate=50000, ot_multiplier=1.5):
    # Tính tiền làm thêm giờ (OT)
    # Calculate overtime pay
    pass

def calculate_kpi_bonus(basic_salary, rank):
    # Tính tiền thưởng theo xếp loại KPI
    # Calculate bonus based on KPI rank
    pass

def calculate_insurance(insurance_salary):
    # Tính tổng tiền bảo hiểm 10.5% khấu trừ
    # Calculate 10.5% insurance deduction
    pass

def calculate_income_tax(total_income, dependents=0):
    # Tính thuế thu nhập cá nhân theo biểu lũy tiến
    # Calculate progressive personal income tax
    pass

def print_payslip(name, base_salary, ot_pay, kpi_bonus, insurance, tax, net_salary):
    # In bảng phiếu lương chi tiết
    # Print formatted payslip
    pass

def main():
    # Nhập thông tin nhân viên, gọi các hàm và xuất kết quả
    # Input employee details, call functions and display payslip
    pass

if __name__ == "__main__":
    main()
