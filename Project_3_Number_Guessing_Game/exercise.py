# ==============================================================================
# PROJECT 3: GAME ĐOÁN SỐ BÍ MẬT / SECRET NUMBER GUESSING GAME
# ==============================================================================

# [MỤC TIÊU / GOAL]
# Luyện tập: Hàm (function), Cấu trúc rẽ nhánh (if - elif - else), Vòng lặp (while/for), Toán tử so sánh và số học.
# Practice: Functions, Conditional statements (if - elif - else), Loops (while/for), Comparison and arithmetic operators.

# [YÊU CẦU ĐỀ BÀI / EXERCISE REQUIREMENTS]
# 1. Viết hàm chon_muc_do() cho phép người chơi chọn cấp độ khó và trả về giới hạn số và số lượt đoán:
# 1. Write a function chon_muc_do() allowing players to choose difficulty, returning max range and attempts:
#    - Mức 1 (De / Easy): Khoảng 1 đến 50, có 10 lượt đoán.
#    - Level 1 (Easy): Range 1 to 50, 10 attempts.
#    - Mức 2 (Kho / Hard): Khoảng 1 đến 100, có 6 lượt đoán.
#    - Level 2 (Hard): Range 1 to 100, 6 attempts.

# 2. Viết hàm kiem_tra_doan(so_doan, so_bi_mat) so sánh số đoán với số bí mật:
# 2. Write a function kiem_tra_doan(so_doan, so_bi_mat) comparing guess with secret number:
#    - Nếu so_doan == so_bi_mat: trả về "Chinh xac".
#    - If so_doan == so_bi_mat: return "Correct".
#    - Nếu so_doan > so_bi_mat: trả về "Qua lon".
#    - If so_doan > so_bi_mat: return "Too high".
#    - Nếu so_doan < so_bi_mat: trả về "Qua nho".
#    - If so_doan < so_bi_mat: return "Too low".

# 3. Viết hàm tinh_diem(so_luot_con_lai, he_so) tính điểm thắng theo công thức: so_luot_con_lai * 10 * he_so.
# 3. Write a function tinh_diem(so_luot_con_lai, he_so) calculating winning score: so_luot_con_lai * 10 * he_so.

# 4. Sử dụng vòng lặp while để cho phép người chơi đoán cho đến khi đoán đúng hoặc hết số lượt.
# 4. Use a while loop to let the player guess until they guess correctly or run out of attempts.

# 5. Dùng câu lệnh if kiểm tra nếu khoảng cách abs(so_doan - so_bi_mat) <= 3 thì in thêm gợi ý "Rất gần rồi!".
# 5. Use an if statement checking if abs(so_doan - so_bi_mat) <= 3 to print extra hint "Very close!".

# ==============================================================================
# [KHUNG BÀI TẬP / STARTER CODE]
# ==============================================================================

import random

def chon_muc_do():
    # Nhập lựa chọn mức độ và trả về (gioi_han_tren, so_luot, he_so)
    # Input difficulty choice and return (max_num, attempts, multiplier)
    pass

def kiem_tra_doan(so_doan, so_bi_mat):
    # Dùng if - elif - else để so sánh số đoán và số bí mật
    # Use if - elif - else to compare guess and secret number
    pass

def tinh_diem(so_luot_con_lai, he_so):
    # Tính và trả về điểm số đạt được
    # Calculate and return earned score
    pass

def choi_game():
    # Tạo số bí mật ngẫu nhiên: so_bi_mat = random.randint(1, gioi_han_tren)
    # Generate secret number: so_bi_mat = random.randint(1, max_num)
    
    # Dùng vòng lặp while nhận số đoán của người chơi
    # Use while loop to receive player's guesses
    pass

def main():
    # Vòng lặp cho phép người chơi chơi nhiều ván
    # Loop allowing player to play multiple rounds
    pass

if __name__ == "__main__":
    main()
