# ==============================================================================
# PROJECT 1: XẾP LOẠI HỌC LỰC HỌC SINH / STUDENT GRADE CLASSIFIER
# ==============================================================================

# ------------------------------------------------------------------------------
# [TIẾNG VIỆT] ĐỀ BÀI: XẾP LOẠI HỌC LỰC HỌC SINH
# ------------------------------------------------------------------------------
# MỤC TIÊU:
# Luyện tập: Hàm (function), Cấu trúc rẽ nhánh (if - elif - else), Vòng lặp (loops), Toán tử cơ bản.
#
# YÊU CẦU:
# 1. Viết hàm calculate_average_score(math, literature, english) nhận vào điểm 3 môn và trả về điểm trung bình.
# 2. Điểm trung bình được tính theo công thức: (math + literature + english) / 3.
# 3. Viết hàm classify_academic_rank(average_score) nhận vào điểm trung bình và trả về kết quả xếp loại học lực:
#    - Điểm >= 9.0: "Xuat sac"
#    - Điểm >= 8.0 và < 9.0: "Gioi"
#    - Điểm >= 6.5 và < 8.0: "Kha"
#    - Điểm >= 5.0 và < 6.5: "Trung binh"
#    - Điểm < 5.0: "Yeu"
# 4. Viết hàm check_valid_score(score) kiểm tra điểm có nằm trong khoảng từ 0 đến 10 hay không.
# 5. Dùng vòng lặp for hoặc while để nhập điểm cho n học sinh do người dùng chỉ định.
# 6. Sử dụng biến đếm để thống kê số lượng học sinh đạt loại Gioi/Xuat sac và số học sinh Yeu.

# ------------------------------------------------------------------------------
# [ENGLISH] EXERCISE: STUDENT GRADE CLASSIFIER
# ------------------------------------------------------------------------------
# GOALS:
# Practice: Functions, Conditional statements (if - elif - else), Loops, Basic operators.
#
# REQUIREMENTS:
# 1. Write a function calculate_average_score(math, literature, english) taking 3 subject scores and returning the average score.
# 2. The average score is calculated using the formula: (math + literature + english) / 3.
# 3. Write a function classify_academic_rank(average_score) taking the average score and returning the academic rank:
#    - Score >= 9.0: "Excellent"
#    - Score >= 8.0 and < 9.0: "Good"
#    - Score >= 6.5 and < 8.0: "Fair"
#    - Score >= 5.0 and < 6.5: "Average"
#    - Score < 5.0: "Weak"
# 4. Write a function check_valid_score(score) to check if the score is between 0 and 10.
# 5. Use a for or while loop to input scores for n students specified by the user.
# 6. Use counter variables to count how many students achieved Good/Excellent and Weak ranks.

# DELETE "pass" in each function and try to solve it by yourself. 

# ==============================================================================
# [STARTER CODE]
# ==============================================================================

def check_valid_score(score):
    # Kiểm tra điểm hợp lệ (từ 0 đến 10)
    # Check if score is valid (between 0 and 10)
    pass

def calculate_average_score(math, literature, english):
    # Tính và trả về điểm trung bình 3 môn
    # Calculate and return the average score of 3 subjects
    pass

def classify_academic_rank(average_score):
    # Dùng if - elif - else để xếp loại học lực
    # Use if - elif - else to classify academic rank
    pass

def main():
    # Nhập số lượng học sinh n
    # Input number of students n
    
    # Dùng vòng lặp lặp n lần để nhập điểm và in kết quả cho từng học sinh
    # Use a loop to repeat n times to input scores and print results for each student
    
    # In ra tổng kết số học sinh giỏi và số học sinh yếu
    # Print summary of good students and weak students
    pass

if __name__ == "__main__":
    main()
