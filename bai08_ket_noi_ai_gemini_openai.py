"""
BÀI 08: KẾT NỐI PYTHON VỚI NÃO BỘ AI (GOOGLE GEMINI / OPENAI)
Dành cho học sinh lớp 7

Mục tiêu:
- Học cách kết nối Python trực tiếp với máy chủ AI (Google Gemini hoặc OpenAI)
- Hiểu khái niệm 'System Prompt' (Định hình tính cách/vai trò của AI)
- Xây dựng ứng dụng "Gia sư AI giải bài tập và dịch thuật"
"""

import os

# ==============================================================================
# BƯỚC 1: ĐIỀN API KEY CỦA BẠN VÀO ĐÂY (Lấy miễn phí tại https://aistudio.google.com/)
# ==============================================================================
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "DÁN_API_KEY_CỦA_BẠN_VÀO_ĐÂY")

def goi_gemini_ai(cau_hoi, vai_tro_he_thong="Bạn là gia sư AI thông minh và thân thiện cho học sinh lớp 7."):
    """
    Hàm gửi câu hỏi lên Google Gemini AI và nhận câu trả lời
    """
    # Nếu chưa có API Key thực, bot sẽ chạy ở chế độ mô phỏng để học sinh vẫn thực hành được
    if GEMINI_API_KEY == "DÁN_API_KEY_CỦA_BẠN_VÀO_ĐÂY":
        return (
            "[MÔ PHỎNG AI - Chưa nhập API Key thực]:\n"
            f"Tôi là AI Gia Sư! Bạn vừa hỏi: '{cau_hoi}'.\n"
            "👉 Hãy dán mã API Key miễn phí từ https://aistudio.google.com/ vào biến GEMINI_API_KEY ở dòng 16 để kích hoạt não bộ AI thật nhé!"
        )

    try:
        # Cách 1: Sử dụng thư viện google-genai mới nhất
        from google import genai
        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{vai_tro_he_thong}\n\nCâu hỏi của học sinh: {cau_hoi}"
        )
        return response.text

    except Exception as e:
        # Fallback thử cách 2 nếu máy dùng thư viện requests thuần
        try:
            import requests
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
            headers = {"Content-Type": "application/json"}
            payload = {
                "contents": [{
                    "parts": [{"text": f"{vai_tro_he_thong}\n\nCâu hỏi: {cau_hoi}"}]
                }]
            }
            res = requests.post(url, json=payload, headers=headers, timeout=15)
            data = res.json()
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as err:
            return f"Lỗi kết nối tới AI: {err}"


# ==============================================================================
# BƯỚC 2: CHẠY THỬ NGHIỆM CHƯƠNG TRÌNH GIA SƯ AI
# ==============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("🎓 CHƯƠNG TRÌNH GIA SƯ AI THÔNG MINH LỚP 7 🎓")
    print("=" * 60)
    print("Bạn có thể hỏi mọi câu hỏi về: Toán, Khoa học, Lịch sử, Tiếng Anh...\n")

    prompt_gia_su = (
        "Bạn là một gia sư AI siêu dễ thương dành cho học sinh lớp 7. "
        "Hãy giải thích ngắn gọn, dễ hiểu, có kèm ví dụ minh họa và luôn động viên các em học tập."
    )

    while True:
        cau_hoi = input("\nHọc sinh: ")
        if cau_hoi.lower().strip() in ["exit", "quit", "thoat", "tạm biệt"]:
            print("Gia sư AI: Chúc em ôn bài thật tốt nhé! Hẹn gặp lại! 👋")
            break

        if not cau_hoi.strip():
            continue

        print("\n⏳ Gia sư AI đang suy nghĩ câu trả lời...")
        cau_tra_loi = goi_gemini_ai(cau_hoi, vai_tro_he_thong=prompt_gia_su)
        print(f"\n🤖 Gia sư AI:\n{cau_tra_loi}\n")
        print("-" * 50)

# ----------------------------------------------------
# 📝 BÀI TẬP THỰC HÀNH TẠI NHÀ CHO HỌC SINH:
# 1. Đổi `vai_tro_he_thong` thành: "Bạn là một nhà thông thái lịch sử thời Trần, xưng hô 'ta' và 'ngươi' để kể chuyện lịch sử."
# 2. Đổi `vai_tro_he_thong` thành: "Bạn là giáo viên bản xứ dạy tiếng Anh, luôn sửa lỗi chính tả ngữ pháp cho học sinh."
# ----------------------------------------------------
