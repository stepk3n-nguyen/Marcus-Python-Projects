"""
BÀI 06: HÀM (FUNCTION - DEF) & DỰ ÁN TRỢ LÝ ẢO THUẦN PYTHON
Dành cho học sinh lớp 7

Mục tiêu:
- Hiểu khái niệm Hàm (def): Chia nhỏ bài toán lớn thành các khối chức năng độc lập
- Nắm được cách truyền tham số vào hàm và giá trị trả về (return)
- Xây dựng sản phẩm kết thúc Giai đoạn 1: "Trợ Lý Học Tập Mini"
"""

import datetime
import random

# ====================================================
# KHAI BÁO CÁC HÀM CHỨC NĂNG (MODULES)
# ====================================================

def lay_loi_chao():
    """Hàm trả về câu chào ngẫu nhiên"""
    cau_chao = [
        "Xin chào! Trợ lý lớp 7 sẵn sàng hỗ trợ bạn.",
        "Chào bạn nhé, chúc bạn buổi học vui vẻ!",
        "Hi! Hôm nay chúng ta cùng học những điều mới mẻ nào."
    ]
    return random.choice(cau_chao)


def xem_ngay_gio():
    """Hàm lấy thông tin thời gian hiện tại"""
    now = datetime.datetime.now()
    return now.strftime("Bây giờ là %H:%M:%S ngày %d/%m/%Y")


def may_tinh_mini(bieu_thuc):
    """Hàm tính toán biểu thức số học an toàn"""
    try:
        # Thay thế ký hiệu nhân x thành * nếu người dùng quen tay
        bieu_thuc_chuan = bieu_thuc.replace("x", "*").replace("X", "*").replace(":", "/")
        ket_qua = eval(bieu_thuc_chuan)
        return f"Kết quả của phép tính '{bieu_thuc}' là: {ket_qua}"
    except Exception:
        return "Xin lỗi, mình không hiểu phép tính này. Bạn hãy nhập dạng ví dụ: 25 * 4 hoặc 100 / 5"


def ke_chuyen_vui():
    """Hàm kể một mẩu chuyện cười xả stress"""
    chuyen_cuoi = [
        "Thầy giáo hỏi Tí: 'Nếu có 5 quả táo, em cho bạn 2 quả thì còn mấy quả?'\nTí: 'Dạ thưa thầy, em không cho bạn quả nào đâu ạ!' 😂",
        "Hai con cá đang bơi dưới nước, một con hỏi: 'Cậu có thấy nước hôm nay ướt không?' 🐟",
        "Vì sao con chim cánh cụt không bao giờ đi máy bay?\nVì nó đã có cánh rồi nhưng thích đi bộ hơn! 🐧"
    ]
    return random.choice(chuyen_cuoi)


def xu_ly_yeu_cau(tin_nhan):
    """
    Hàm trung tâm điều phối và xử lý toàn bộ tin nhắn người dùng
    """
    text = tin_nhan.lower().strip()

    if not text:
        return "Bạn hãy gõ gì đó để trò chuyện cùng mình nhé!"

    if "chào" in text or "hi" in text or "hello" in text:
        return lay_loi_chao()

    elif "mấy giờ" in text or "thời gian" in text or "ngày" in text:
        return xem_ngay_gio()

    elif "tính" in text or "phép tính" in text or "+" in text or "-" in text or "*" in text or "/" in text:
        # Tách phần phép tính
        phep_tinh = text.replace("tính", "").replace("phép tính", "").strip()
        if phep_tinh:
            return may_tinh_mini(phep_tinh)
        return "Hãy nhập phép tính bạn muốn tính (ví dụ: tính 12 * 8)"

    elif "chuyện cười" in text or "hài" in text or "vui" in text:
        return ke_chuyen_vui()

    elif "tạm biệt" in text or "bye" in text:
        return "TẠM_BIỆT"

    else:
        return "Câu hỏi này mình chưa được lập trình. Nhưng đừng lo, từ bài sau chúng ta sẽ nối vào AI để bot trả lời được mọi thứ!"


# ====================================================
# CHƯƠNG TRÌNH CHÍNH (MAIN LOOP)
# ====================================================
if __name__ == "__main__":
    print("=" * 60)
    print("🌟 SẢN PHẨM: TRỢ LÝ HỌC TẬP THUẦN PYTHON (PHIÊN BẢN HÀM) 🌟")
    print("=" * 60)
    print("Bạn có thể gõ: 'chào', 'mấy giờ', 'tính 45 * 2', 'kể chuyện vui', 'tạm biệt'\n")

    while True:
        nguoi_dung = input("Bạn: ")
        phan_hoi = xu_ly_yeu_cau(nguoi_dung)

        if phan_hoi == "TẠM_BIỆT":
            print("Bot: Tạm biệt bạn! Hẹn gặp lại trong thế giới AI ở Giai đoạn 2 nhé! 👋")
            break

        print(f"Bot: {phan_hoi}\n")

# ----------------------------------------------------
# 📝 BÀI TẬP THỰC HÀNH TẠI NHÀ CHO HỌC SINH:
# 1. Viết thêm một hàm mới: `def tao_mat_khau_ngau_nhien(do_dai=8)` 
#    tạo ra một mật khẩu ngẫu nhiên gồm các chữ cái và số cho người dùng.
# 2. Kết nối hàm vừa viết vào hàm `xu_ly_yeu_cau()` khi người dùng gõ "tạo mật khẩu".
# ----------------------------------------------------
