"""
BÀI 09: XÂY DỰNG CHATBOT LAI THÔNG MINH (HYBRID CHATBOT)
=========================================================
KẾT HỢP CODE QUY TẮC (RULE-BASED) & TRÍ TUỆ NHÂN TẠO (AI)
(Đúng theo mô hình ứng dụng phụ huynh học sinh yêu cầu)

Mô hình hoạt động (Pipeline):
1. Người dùng gửi tin nhắn.
2. Hệ thống kiểm tra điều kiện if/elif (Quy tắc cố định do lập trình viên định nghĩa).
   -> Nếu khớp lệnh (vd: xem giờ, tính toán nhanh, thông tin tác giả, mở ứng dụng): 
      ==> Code Python tự xử lý ngay lập tức (Nhanh 0 giây, không tốn tiền API).
3. Nếu KHÔNG khớp bất kỳ quy tắc nào:
   ==> Chuyển tiếp (Fallback) câu hỏi đó sang não bộ AI (ChatGPT / Gemini).
   ==> AI suy luận và trả lời câu hỏi mở của người dùng.
"""

import os
import datetime

# ------------------------------------------------------------------------------
# 1. CẤU HÌNH API AI (GOOGLE GEMINI / OPENAI)
# ------------------------------------------------------------------------------
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "DÁN_API_KEY_CỦA_BẠN_VÀO_ĐÂY")

def goi_nao_bo_ai(cau_hoi):
    """Gửi câu hỏi mở sang mô hình AI để suy luận"""
    if GEMINI_API_KEY == "DÁN_API_KEY_CỦA_BẠN_VÀO_ĐÂY":
        return (
            f"[Phản hồi từ Não Bộ AI (Mô phỏng)]:\n"
            f"Tôi là AI! Đối với câu hỏi mở '{cau_hoi}', tôi có thể giải thích chi tiết, "
            f"làm thơ, viết văn hoặc phân tích chuyên sâu cho bạn khi đã gắn API Key thật."
        )

    try:
        from google import genai
        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Hãy trả lời ngắn gọn, thân thiện và hữu ích cho học sinh: {cau_hoi}"
        )
        return response.text
    except Exception:
        # Fallback bằng HTTP Request
        try:
            import requests
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
            res = requests.post(url, json={"contents": [{"parts": [{"text": cau_hoi}]}]}, timeout=15)
            return res.json()["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            return f"Không thể kết nối với máy chủ AI: {e}"


# ------------------------------------------------------------------------------
# 2. BỘ XỬ LÝ TRUNG TÂM: HYBRID DISPATCHER (QUY TẮC + AI)
# ------------------------------------------------------------------------------
def xu_ly_tin_nhan_hybrid(tin_nhan):
    """
    Hàm phân loại tin nhắn:
    - Trả về (nguon_goc, cau_tra_loi)
    - nguon_goc: "QUY_TAC_PYTHON" hoặc "TRI_TUE_NHAN_TAO_AI"
    """
    text = tin_nhan.lower().strip()

    if not text:
        return "QUY_TAC_PYTHON", "Bạn chưa nhập nội dung gì cả!"

    # ==========================================================
    # NHÓM 1: CÁC CÂU HỎI & LỆNH ĐƯỢC LẬP TRÌNH CỐ ĐỊNH (RULE-BASED)
    # ==========================================================

    # Lệnh chào hỏi cơ bản
    if text in ["chào", "chao", "hi", "hello", "xin chào"]:
        return "QUY_TAC_PYTHON", "Xin chào! Mình là Chatbot Lai Thông Minh (Hybrid AI Bot) lớp 7."

    # Lệnh tra cứu giờ hệ thống
    elif "mấy giờ" in text or "thời gian" in text:
        gio = datetime.datetime.now().strftime("%H:%M:%S")
        return "QUY_TAC_PYTHON", f"Hiện tại trên đồng hồ máy tính là: {gio}"

    # Lệnh tra cứu ngày tháng
    elif "ngày mấy" in text or "hôm nay là ngày" in text:
        ngay = datetime.datetime.now().strftime("%d/%m/%Y")
        return "QUY_TAC_PYTHON", f"Hôm nay là ngày {ngay}."

    # Lệnh tính toán nhanh bằng máy tính tích hợp
    elif text.startswith("tính ") or text.startswith("tinh "):
        bieu_thuc = text.replace("tính", "").replace("tinh", "").strip()
        try:
            ket_qua = eval(bieu_thuc)
            return "QUY_TAC_PYTHON", f"Kết quả tính nhẩm nhanh: {bieu_thuc} = {ket_qua}"
        except Exception:
            return "QUY_TAC_PYTHON", "Biểu thức toán chưa đúng định dạng (Ví dụ: tính 15 * 6)"

    # Thông tin nhóm phát triển
    elif "tác giả" in text or "ai tạo ra bạn" in text or "bạn là ai" in text:
        return "QUY_TAC_PYTHON", "Tôi là sản phẩm kết hợp giữa Python Lớp 7 và Trí tuệ Nhân tạo AI!"

    # ==========================================================
    # NHÓM 2: CÂU HỎI MỞ / KHÔNG KHỚP QUY TẮC -> CHUYỂN SANG CHO AI
    # ==========================================================
    else:
        # Gọi sang não bộ AI (Gemini/ChatGPT)
        tra_loi_ai = goi_nao_bo_ai(tin_nhan)
        return "TRI_TUE_NHAN_TAO_AI", tra_loi_ai


# ------------------------------------------------------------------------------
# 3. CHƯƠNG TRÌNH CHẠY CHÍNH (GIAO DIỆN CONSOLE)
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 65)
    print("🤖 HỆ THỐNG CHATBOT LAI (HYBRID BOT): PYTHON + AI 🤖")
    print("=" * 65)
    print("💡 THỬ NGHIỆM:")
    print("  1. Câu hỏi quy tắc: 'chào', 'mấy giờ', 'hôm nay là ngày', 'tính 100 / 4'")
    print("     -> Python sẽ xử lý trực tiếp lập tức.")
    print("  2. Câu hỏi mở: 'Tại sao bầu trời màu xanh?', 'Viết 1 đoạn văn về mẹ'...")
    print("     -> Bot sẽ tự động gọi sang Não bộ AI để giải đáp.")
    print("=" * 65 + "\n")

    while True:
        user_input = input("\n👤 Bạn: ")
        if user_input.lower().strip() in ["exit", "thoat", "tạm biệt"]:
            print("🤖 Bot: Hẹn gặp lại bạn!")
            break

        nguon, phan_hoi = xu_ly_tin_nhan_hybrid(user_input)

        if nguon == "QUY_TAC_PYTHON":
            print(f"⚙️ [Nguồn: Lập trình Python xử lý trực tiếp]")
            print(f"🤖 Bot: {phan_hoi}")
        else:
            print(f"🧠 [Nguồn: Trí tuệ Nhân tạo AI (Gemini/ChatGPT) xử lý]")
            print(f"🤖 Bot:\n{phan_hoi}")

# ----------------------------------------------------
# 📝 BÀI TẬP THỰC HÀNH TẠI NHÀ CHO HỌC SINH:
# 1. Thêm 2 quy tắc cứng mới vào NHÓM 1:
#    - Khi gõ "bật đèn" hoặc "tắt đèn" -> In thông báo mô phỏng điều khiển nhà thông minh (Smart Home).
# 2. Thử nghiệm hỏi 3 câu hỏi khó về khoa học và quan sát AI trả lời.
# ----------------------------------------------------
