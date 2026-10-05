"""
BÀI 12: ĐỒNG BỘ SẢN PHẨM TỐT NGHIỆP: "SMART AI ASSISTANT APP"
=============================================================
DỰ ÁN TỔNG HỢP CUỐI KHÓA CHO HỌC SINH LỚP 7
Tích hợp:
1. Giao diện đồ họa cửa sổ ứng dụng hiện đại (Tkinter Dark Mode)
2. Luồng xử lý đa luồng (Threading) giúp giao diện không bị đơ/lag khi chờ AI trả lời
3. Kiến trúc Hybrid: Rule-based (Lập trình quy tắc Python) + AI Fallback (Google Gemini / OpenAI)
4. Đóng gói ứng dụng thành file .exe độc lập
"""

import os
import datetime
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

# ==============================================================================
# 1. CẤU HÌNH API AI
# ==============================================================================
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "DÁN_API_KEY_CỦA_BẠN_VÀO_ĐÂY")

def goi_api_ai(cau_hoi):
    """Gửi câu hỏi sang não bộ AI"""
    if GEMINI_API_KEY == "DÁN_API_KEY_CỦA_BẠN_VÀO_ĐÂY":
        return (
            "[Mô phỏng Trí tuệ Nhân tạo AI]:\n"
            f"Tôi là AI trợ lý lớp 7! Bạn vừa hỏi câu hỏi mở: '{cau_hoi}'.\n"
            "👉 Hãy dán API Key thật của bạn vào đầu file (dòng 17) để bot kết nối trực tiếp với Google Gemini nhé!"
        )

    try:
        from google import genai
        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Bạn là trợ lý AI thông minh, thân thiện cho học sinh lớp 7. Hãy trả lời ngắn gọn: {cau_hoi}"
        )
        return response.text
    except Exception:
        try:
            import requests
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
            res = requests.post(url, json={"contents": [{"parts": [{"text": cau_hoi}]}]}, timeout=15)
            return res.json()["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            return f"⚠️ Không thể kết nối máy chủ AI: {e}"


# ==============================================================================
# 2. XỬ LÝ LOGIC LAI (HYBRID LOGIC)
# ==============================================================================
def xu_ly_tin_nhan(tin_nhan):
    """
    Phân luồng tin nhắn:
    - Nếu là câu lệnh/quy tắc định sẵn -> Code Python tự trả lời ngay.
    - Nếu là câu hỏi mở -> Gửi sang cho AI.
    """
    text = tin_nhan.lower().strip()

    # Nhóm 1: Quy tắc lập trình cố định (Rule-based)
    if text in ["chào", "chao", "hi", "hello"]:
        return "PYTHON", "Xin chào bạn! Mình là Trợ Lý Ảo Đa Năng Lớp 7 sẵn sàng phục vụ!"

    elif "mấy giờ" in text or "thời gian" in text:
        gio = datetime.datetime.now().strftime("%H:%M:%S")
        return "PYTHON", f"Bây giờ là {gio} trên đồng hồ máy tính của bạn."

    elif "ngày mấy" in text or "hôm nay là ngày" in text:
        ngay = datetime.datetime.now().strftime("%d/%m/%Y")
        return "PYTHON", f"Hôm nay là ngày {ngay}."

    elif text.startswith("tính ") or text.startswith("tinh "):
        bieu_thuc = text.replace("tính", "").replace("tinh", "").strip()
        try:
            ket_qua = eval(bieu_thuc)
            return "PYTHON", f"Kết quả máy tính mini: {bieu_thuc} = {ket_qua}"
        except Exception:
            return "PYTHON", "Phép tính không hợp lệ (Ví dụ đúng: tính 25 * 4 + 10)"

    elif "tác giả" in text or "ai làm ra bạn" in text:
        return "PYTHON", "Sản phẩm được lập trình bởi học sinh tài năng của Khóa học Python & AI!"

    # Nhóm 2: Câu hỏi mở chuyển sang AI
    else:
        ket_qua_ai = goi_api_ai(tin_nhan)
        return "AI", ket_qua_ai


# ==============================================================================
# 3. THIẾT KẾ GIAO DIỆN ỨNG DỤNG (GUI) & ĐA LUỒNG (THREADING)
# ==============================================================================
class SmartAssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌟 SMART AI ASSISTANT - HỌC SINH LỚP 7")
        self.root.geometry("580x680")
        self.root.configure(bg="#1E1E2E")

        # Header
        header = tk.Frame(root, bg="#313244", pady=10)
        header.pack(fill=tk.X)

        title = tk.Label(
            header,
            text="🤖 TRỢ LÝ THÔNG MINH PYTHON & AI",
            font=("Segoe UI", 13, "bold"),
            bg="#313244",
            fg="#89B4FA"
        )
        title.pack()

        subtitle = tk.Label(
            header,
            text="Kết hợp Lập trình Quy tắc & Trí tuệ Nhân tạo",
            font=("Segoe UI", 9, "italic"),
            bg="#313244",
            fg="#A6ADC8"
        )
        subtitle.pack()

        # Chat Area
        self.chat_display = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            state=tk.DISABLED,
            bg="#181825",
            fg="#CDD6F4",
            font=("Segoe UI", 11),
            padx=12,
            pady=12
        )
        self.chat_display.pack(padx=15, pady=10, fill=tk.BOTH, expand=True)

        # Style Tags
        self.chat_display.tag_config("user_tag", foreground="#A6E3A1", font=("Segoe UI", 11, "bold"))
        self.chat_display.tag_config("python_tag", foreground="#89B4FA")
        self.chat_display.tag_config("ai_tag", foreground="#F9E2AF")

        # Input Area
        input_frame = tk.Frame(root, bg="#1E1E2E")
        input_frame.pack(fill=tk.X, padx=15, pady=(0, 15))

        self.user_entry = tk.Entry(
            input_frame,
            font=("Segoe UI", 12),
            bg="#313244",
            fg="#FFFFFF",
            insertbackground="white"
        )
        self.user_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=6, padx=(0, 10))
        self.user_entry.bind("<Return>", self.gui_tin_nhan_thread)

        self.btn_send = tk.Button(
            input_frame,
            text="Gửi 🚀",
            font=("Segoe UI", 11, "bold"),
            bg="#89B4FA",
            fg="#11111B",
            activebackground="#B4BEFE",
            padx=16,
            command=self.gui_tin_nhan_thread
        )
        self.btn_send.pack(side=tk.RIGHT)

        # Welcome message
        self.them_tin_nhan("Bot", "Xin chào! Mình có thể giúp gì cho bạn hôm nay?\n(Thử gõ: 'chào', 'mấy giờ', 'tính 12 * 8' hoặc hỏi bất kỳ câu hỏi nào để AI trả lời!)", "python_tag")

    def them_tin_nhan(self, nguoi_gui, noi_dung, tag):
        self.chat_display.config(state=tk.NORMAL)
        if nguoi_gui == "Bạn":
            self.chat_display.insert(tk.END, f"👤 Bạn: {noi_dung}\n", tag)
        elif tag == "python_tag":
            self.chat_display.insert(tk.END, f"⚙️ Bot (Python): {noi_dung}\n\n", tag)
        else:
            self.chat_display.insert(tk.END, f"🧠 Bot (AI): {noi_dung}\n\n", tag)
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)

    def gui_tin_nhan_thread(self, event=None):
        tin_nhan = self.user_entry.get().strip()
        if not tin_nhan:
            return

        self.them_tin_nhan("Bạn", tin_nhan, "user_tag")
        self.user_entry.delete(0, tk.END)

        # Chạy việc xử lý trong 1 luồng riêng (Thread) để giao diện không bị giật lag
        threading.Thread(target=self.xu_ly_va_tra_loi, args=(tin_nhan,), daemon=True).start()

    def xu_ly_va_tra_loi(self, tin_nhan):
        nguon, tra_loi = xu_ly_tin_nhan(tin_nhan)
        tag = "python_tag" if nguon == "PYTHON" else "ai_tag"
        self.them_tin_nhan("Bot", tra_loi, tag)


# ==============================================================================
# HƯỚNG DẪN ĐÓNG GÓI RA FILE .EXE CHO HỌC SINH MANG VỀ KHOE BA MẸ:
# ==============================================================================
"""
Bước 1: Mở Terminal tại thư mục này
Bước 2: Cài đặt công cụ đóng gói:
        pip install pyinstaller
Bước 3: Chạy lệnh xuất file exe:
        pyinstaller --noconsole --onefile bai12_smart_assistant_app.py
Bước 4: Vào thư mục 'dist', bạn sẽ thấy file 'bai12_smart_assistant_app.exe' có thể chạy trên bất kỳ máy tính Windows nào!
"""

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartAssistantApp(root)
    root.mainloop()
