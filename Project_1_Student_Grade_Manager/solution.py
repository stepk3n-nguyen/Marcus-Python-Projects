# ==============================================================================
# PROJECT 1: XẾP LOẠI HỌC LỰC HỌC SINH / STUDENT GRADE CLASSIFIER
# LỜI GIẢI HOÀN CHỈNH / FULL SOLUTION
# ==============================================================================

# 1. Hàm kiểm tra tính hợp lệ của điểm số
# 1. Function to validate score
def check_valid_score(score):
    # Điểm phải lớn hơn hoặc bằng 0 và nhỏ hơn hoặc bằng 10
    # Score must be greater than or equal to 0 and less than or equal to 10
    if score >= 0 and score <= 10:
        return True
    else:
        return False


# 2. Hàm tính điểm trung bình của 3 môn học
# 2. Function to calculate the average score of 3 subjects
def calculate_average_score(math, literature, english):
    # Dùng toán tử cộng để tính tổng điểm
    # Use addition operator to calculate total score
    total_score = math + literature + english
    
    # Dùng toán tử chia để tính điểm trung bình
    # Use division operator to calculate average score
    average_score = total_score / 3
    
    # Trả về điểm trung bình được làm tròn 2 chữ số
    # Return average score rounded to 2 decimal places
    return round(average_score, 2)


# 3. Hàm phân loại học lực dựa trên điểm trung bình
# 3. Function to classify academic rank based on average score
def academic_rank(average_score):
    # Sử dụng cấu trúc rẽ nhánh if - elif - else
    # Use conditional statement if - elif - else
    if average_score >= 9.0:
        return "Excellent"
    elif average_score >= 8.0:
        return "Good"
    elif average_score >= 6.5:
        return "Fair"
    elif average_score >= 5.0:
        return "Average"
    else:
        return "Weak"


# 4. Hàm chính điều khiển chương trình
# 4. Main function to run the program
def main():
    print("=== STUDENT GRADE CLASSIFICATION PROGRAM ===")

    # Nhập số lượng học sinh cần tính điểm
    # Input the number of students to grade
    number_of_students = int(input("Enter number of students: "))

    # Khởi tạo các biến đếm thống kê
    # Initialize counter variables for statistics
    good_students = 0
    weak_students = 0

    # Dùng vòng lặp for chạy từ học sinh thứ 1 đến học sinh thứ n
    # Use a for loop running from student 1 to student n
    for i in range(1, number_of_students + 1):
        print(f"\n--- Input student information {i} ---")
        name = input("Enter student name: ")

        # Nhập điểm môn Toán và kiểm tra bằng vòng lặp while
        # Input Math score and validate using while loop
        math = float(input("Enter Math score (0-10): "))
        while not check_valid_score(math):
            print("Invalid score! Please enter again.")
            math = float(input("Enter Math score (0-10): "))

        # Nhập điểm môn Văn
        # Input Literature score
        literature = float(input("Enter Literature score (0-10): "))
        while not check_valid_score(literature):
            print("Invalid score! Please enter again.")
            literature = float(input("Enter Literature score (0-10): "))

        # Nhập điểm môn Tiếng Anh
        # Input English score
        english = float(input("Enter English score (0-10): "))
        while not check_valid_score(english):
            print("Invalid score! Please enter again.")
            english = float(input("Enter English score (0-10): "))

        # Gọi hàm tính điểm trung bình
        # Call function to calculate average score
        average_score = calculate_average_score(math, literature, english)

        # Gọi hàm xếp loại học lực
        # Call function to classify academic rank
        rank = academic_rank(average_score)

        # In kết quả của từng học sinh
        # Print results for each student
        print(f"-> Student: {name} | Avg Score: {average_score} | Rank: {rank}")

        # Thống kê số lượng học sinh bằng if - else và toán tử tăng biến đếm
        # Count number of students using if - else and increment operator
        if average_score >= 8.0:
            good_students = good_students + 1
        elif average_score < 5.0:
            weak_students = weak_students + 1

    # In phần tổng kết thống kê sau khi kết thúc vòng lặp
    # Print statistics summary after the loop ends
    print("\n================ SUMMARY ================")
    print(f"Total students: {number_of_students}")
    print(f"Good & Excellent students: {good_students}")
    print(f"Weak students: {weak_students}")
    print("============================================")


if __name__ == "__main__":
    main()
