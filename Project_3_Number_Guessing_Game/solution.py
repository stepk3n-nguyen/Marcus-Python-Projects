# ==============================================================================
# PROJECT 3: GAME ĐOÁN SỐ BÍ MẬT / SECRET NUMBER GUESSING GAME
# LỜI GIẢI HOÀN CHỈNH / FULL SOLUTION
# ==============================================================================

import random

# 1. Hàm chọn mức độ khó của trò chơi
# 1. Function to select game difficulty level
def chon_muc_do():
    print("\n--- CHỌN MỨC ĐỘ KHÓ / SELECT DIFFICULTY ---")
    print("1. Dễ (1 - 50, 10 lượt đoán) / Easy (1 - 50, 10 attempts)")
    print("2. Khó (1 - 100, 6 lượt đoán) / Hard (1 - 100, 6 attempts)")

    while True:
        lua_chon = input("Nhập lựa chọn (1 hoặc 2) / Enter choice (1 or 2): ")
        
        # Dùng if - elif - else để gán thông số tương ứng
        # Use if - elif - else to assign corresponding parameters
        if lua_chon == "1":
            # Trả về: (giới hạn số, số lượt đoán, hệ số điểm)
            # Return: (max_range, max_attempts, score_multiplier)
            return 50, 10, 1
        elif lua_chon == "2":
            return 100, 6, 2
        else:
            print("Lựa chọn không hợp lệ! Vui lòng nhập 1 hoặc 2.")
            print("Invalid choice! Please enter 1 or 2.")


# 2. Hàm so sánh số đoán với số bí mật
# 2. Function to compare guess with secret number
def kiem_tra_doan(so_doan, so_bi_mat):
    # Dùng các toán tử so sánh ==, >, <
    # Use comparison operators ==, >, <
    if so_doan == so_bi_mat:
        return "Chinh xac / Correct"
    elif so_doan > so_bi_mat:
        return "Qua lon / Too high"
    else:
        return "Qua nho / Too low"


# 3. Hàm tính điểm số đạt được khi thắng
# 3. Function to calculate score earned upon winning
def tinh_diem(so_luot_con_lai, he_so):
    # Dùng toán tử nhân tính điểm
    # Use multiplication operator to calculate score
    diem = so_luot_con_lai * 10 * he_so
    return diem


# 4. Hàm thực hiện một ván chơi
# 4. Function to play one round of the game
def choi_game():
    gioi_han_tren, so_luot_toi_da, he_so = chon_muc_do()
    
    # Máy tính sinh một số nguyên ngẫu nhiên từ 1 đến gioi_han_tren
    # Computer generates a random integer from 1 to max_range
    so_bi_mat = random.randint(1, gioi_han_tren)
    
    print(f"\n=> Máy tính đã chọn một số bí mật từ 1 đến {gioi_han_tren}.")
    print(f"=> The computer picked a secret number from 1 to {gioi_han_tren}.")
    print(f"=> Bạn có tổng cộng {so_luot_toi_da} lượt đoán.")
    print(f"=> You have a total of {so_luot_toi_da} attempts.")

    luot_hien_tai = 1
    da_thang = False

    # Dùng vòng lặp while để đếm số lượt đoán
    # Use a while loop to count attempts
    while luot_hien_tai <= so_luot_toi_da:
        so_doan = int(input(f"\n[Lượt {luot_hien_tai}/{so_luot_toi_da}] Nhập số bạn đoán / Enter your guess: "))

        # Gọi hàm kiểm tra kết quả
        # Call function to check result
        phan_hoi = kiem_tra_doan(so_doan, so_bi_mat)

        if phan_hoi == "Chinh xac / Correct":
            da_thang = True
            so_luot_con_lai = so_luot_toi_da - luot_hien_tai + 1
            diem_so = tinh_diem(so_luot_con_lai, he_so)
            print("\n🎉 CHÚC MỪNG! BẠN ĐÃ ĐOÁN ĐÚNG SỐ BÍ MẬT!")
            print("🎉 CONGRATULATIONS! YOU GUESSED THE SECRET NUMBER!")
            print(f"Số bí mật là: {so_bi_mat}")
            print(f"Secret number was: {so_bi_mat}")
            print(f"Điểm số của bạn: {diem_so} điểm")
            print(f"Your score: {diem_so} points")
            break  # Thoát vòng lặp khi đã đoán đúng / Exit loop on correct guess
        else:
            print(f"Kết quả / Result: {phan_hoi}")
            
            # Tính khoảng cách giữa số đoán và số bí mật bằng phép trừ và abs()
            # Calculate distance between guess and secret using subtraction and abs()
            khoang_cach = abs(so_doan - so_bi_mat)
            if khoang_cach <= 3:
                print("🔥 Gợi ý nóng: Bạn đang ở rất gần rồi (chỉ lệch <= 3 đơn vị)!")
                print("🔥 Hot hint: You are very close (difference <= 3)!")

        # Tăng biến đếm lượt đoán
        # Increment attempts counter
        luot_hien_tai = luot_hien_tai + 1

    # Kiểm tra điều kiện thua cuộc khi hết lượt đoán
    # Check loss condition when out of attempts
    if not da_thang:
        print("\n💀 RẤT TIẾC! BẠN ĐÃ HẾT LƯỢT ĐOÁN.")
        print("💀 GAME OVER! YOU RAN OUT OF ATTEMPTS.")
        print(f"Số bí mật của ván này là: {so_bi_mat}")
        print(f"The secret number was: {so_bi_mat}")


# 5. Hàm chính điều khiển vòng lặp chơi lại
# 5. Main function controlling game replay loop
def main():
    print("=== TRÒ CHƠI ĐOÁN SỐ THÔNG MINH ===")
    print("=== SMART NUMBER GUESSING GAME ===")

    # Dùng vòng lặp while True để hỏi người chơi có muốn tiếp tục chơi không
    # Use while True loop to ask if the player wants to play again
    while True:
        choi_game()
        
        hoi_tiep_tuc = input("\nBạn có muốn chơi tiếp không? (y/n) / Play again? (y/n): ")
        if hoi_tiep_tuc.lower() != "y":
            print("Cảm ơn bạn đã tham gia trò chơi! Hẹn gặp lại!")
            print("Thank you for playing! See you next time!")
            break


if __name__ == "__main__":
    main()
