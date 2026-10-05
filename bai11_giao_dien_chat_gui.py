"""
BÀI 11: LÀM QUEN GIAO DIỆN ĐỒ HỌA (GUI) VỚI TKINTER
Dành cho học sinh lớp 7

Mục tiêu:
- Hiểu khái niệm Giao diện người dùng (GUI - Graphical User Interface): Cửa sổ, Nút bấm, Ô nhập liệu, Khung tin nhắn
- Sử dụng thư viện đồ họa chuẩn `tkinter` có sẵn trong Python (không cần cài thêm)
- Xây dựng cửa sổ Chatbot trực quan, hiện đại, màu sắc đẹp mắt
"""

import tkinter as tk
from tkinter import scrolledtext

# ==============================================================================
# HÀM XỬ LÝ SỰ KIỆN GỬI TIN NHẮN
# ==============================================================================
def gui_tin_nhan(event=None):
    tin_nhan = o_nhap_lieu.get().strip()
    if not tin_nhan:
        return

    # 1. Hiển thị tin nhắn của Người dùng lên khung chat
    khung_chat.config(state=tk.NORMAL)
    khung_chat.insert(tk.END, f"👤 Bạn: {tin_nhan}\n", "user_tag")
    o_nhap_lieu.delete(0, tk.END)

    # 2. Xử lý logic câu trả lời của Bot
    text = tin_nhan.lower()
    if "chào" in text or "hi" in text or "hello" in text:
        tra_loi = "Xin chào! Rất vui được trò chuyện với bạn trên giao diện đồ họa!"
    elif "mấy giờ" in text or "giờ" in text:
        import datetime
        tra_loi = f"Bây giờ là {datetime.datetime.now().strftime('%H:%M:%S')}."
    elif "tác giả" in text or "ai tạo ra bạn" in text:
        tra_loi = "Mình được lập trình bởi học sinh lớp 7 tài năng!"
    else:
        tra_loi = f"Mình đã nhận được tin nhắn '{tin_nhan}'. Ở bài 12, mình sẽ kết nối AI để trả lời thông minh câu này nhé!"

    # 3. Hiển thị phản hồi của Bot
    khung_chat.insert(tk.END, f"🤖 Bot: {tra_loi}\n\n", "bot_tag")
    khung_chat.config(state=tk.DISABLED)
    khung_chat.see(tk.END)


# ==============================================================================
# THIẾT KẾ CỬA SỔ GIAO DIỆN (GUI WINDOW)
# ==============================================================================
cua_so = tk.Tk()
cua_so.title("🤖 Chatbot Python Lớp 7 - Giao Diện Đồ Họa")
cua_so.geometry("520x600")
cua_so.configure(bg="#1E1E2E")  # Màu nền Dark Mode hiện đại

# Tiêu đề ứng dụng
nhan_tieu_de = tk.Label(
    cua_so,
    text="💬 PHẦN MỀM CHATBOT THÔNG MINH LỚP 7",
    font=("Segoe UI", 13, "bold"),
    bg="#313244",
    fg="#89B4FA",
    pady=10
)
nhan_tieu_de.pack(fill=tk.X)

# Khung hiển thị lịch sử chat
khung_chat = scrolledtext.ScrolledText(
    cua_so,
    wrap=tk.WORD,
    state=tk.DISABLED,
    bg="#181825",
    fg="#CDD6F4",
    font=("Segoe UI", 11),
    padx=10,
    pady=10
)
khung_chat.pack(padx=15, pady=10, fill=tk.BOTH, expand=True)

# Định dạng màu sắc chữ cho Người dùng và Bot
khung_chat.tag_config("user_tag", foreground="#A6E3A1", font=("Segoe UI", 11, "bold"))  # Màu xanh lá
khung_chat.tag_config("bot_tag", foreground="#89B4FA")                                    # Màu xanh dương

# Khung chứa Ô nhập liệu và Nút gửi
khung_nhap = tk.Frame(cua_so, bg="#1E1E2E")
khung_nhap.pack(fill=tk.X, padx=15, pady=(0, 15))

o_nhap_lieu = tk.Entry(
    khung_nhap,
    font=("Segoe UI", 12),
    bg="#313244",
    fg="#FFFFFF",
    insertbackground="white"
)
o_nhap_lieu.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=6, padx=(0, 10))
o_nhap_lieu.bind("<Return>", gui_tin_nhan)  # Bấm phím Enter để gửi

nut_gui = tk.Button(
    khung_nhap,
    text="Gửi 🚀",
    font=("Segoe UI", 11, "bold"),
    bg="#89B4FA",
    fg="#11111B",
    activebackground="#B4BEFE",
    padx=15,
    command=gui_tin_nhan
)
nut_gui.pack(side=tk.RIGHT)

# Tin nhắn chào mừng ban đầu
khung_chat.config(state=tk.NORMAL)
khung_chat.insert(tk.END, "🤖 Bot: Xin chào! Hãy gõ câu hỏi vào ô bên dưới và bấm 'Gửi' hoặc ấn Enter nhé!\n\n", "bot_tag")
khung_chat.config(state=tk.DISABLED)

# Chạy vòng lặp giao diện
if __name__ == "__main__":
    cua_so.mainloop()

# ----------------------------------------------------
# 📝 BÀI TẬP THỰC HÀNH TẠI NHÀ CHO HỌC SINH:
# 1. Thay đổi kích thước cửa sổ (`geometry`) và đổi màu nền yêu thích.
# 2. Thêm một nút bấm "Xóa Lịch Sử Chat" bên cạnh nút Gửi.
# ----------------------------------------------------
