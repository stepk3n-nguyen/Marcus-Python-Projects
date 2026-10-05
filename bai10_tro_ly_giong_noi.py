"""
BÀI 10: TƯƠNG TÁC GIỌNG NÓI CHO AI (TEXT-TO-SPEECH & SPEECH-TO-TEXT)
Dành cho học sinh lớp 7

Mục tiêu:
- Giúp chương trình Python có thể "nói tiếng Việt" bằng thư viện `gTTS` (Google Text-to-Speech) hoặc `pyttsx3`
- (Mở rộng) Biết cách nhận diện giọng nói từ Microphone thành văn bản bằng `speech_recognition`
- Nâng cấp Chatbot thành Trợ lý ảo có khả năng đàm thoại như Siri / Google Assistant
"""

import os
import tempfile

def noi_tieng_viet(noi_dung):
    """
    Hàm phát âm thanh tiếng Việt từ văn bản
    """
    print(f"🔊 Đang phát giọng nói: \"{noi_dung}\"")
    
    # Cách 1: Sử dụng thư viện pyttsx3 (Chạy offline không cần mạng)
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.say(noi_dung)
        engine.runAndWait()
        return
    except ImportError:
        pass

    # Cách 2: Sử dụng gTTS (Google Text-to-Speech - giọng đọc tiếng Việt rất tự nhiên)
    try:
        from gtts import gTTS
        import pygame
        
        # Tạo file âm thanh tạm thời
        tts = gTTS(text=noi_dung, lang='vi')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            temp_path = fp.name
            tts.save(temp_path)
            
        # Khởi tạo pygame để phát file mp3
        pygame.mixer.init()
        pygame.mixer.music.load(temp_path)
        pygame.mixer.music.play()
        
        # Đợi phát xong
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
        pygame.mixer.quit()
        os.remove(temp_path)
    except Exception as e:
        print(f"⚠️ [Chế độ thông báo]: Chưa cài thư viện âm thanh (pip install gTTS pygame pyttsx3) - Nội dung: {noi_dung}")


def nghe_giong_noi():
    """
    Hàm nghe giọng nói từ microphone và chuyển thành văn bản (Speech to Text)
    """
    try:
        import speech_recognition as sr
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("\n🎤 Đang lắng nghe... Hãy nói điều gì đó vào micro:")
            r.adjust_for_ambient_noise(source, duration=0.8)
            audio = r.listen(source, timeout=5)
            
        print("⏳ Đang xử lý giọng nói...")
        van_ban = r.recognize_google(audio, language="vi-VN")
        print(f"🗣️ Bạn vừa nói: '{van_ban}'")
        return van_ban
    except Exception:
        print("⚠️ Không phát hiện Micro hoặc chưa cài đặt thư viện 'speech_recognition' và 'pyaudio'.")
        # Chuyển sang nhập văn bản thông thường
        return input("👉 Nhập câu nói của bạn bằng bàn phím: ")


# ====================================================
# CHƯƠNG TRÌNH THỬ NGHIỆM TRỢ LÝ GIỌNG NÓI
# ====================================================
if __name__ == "__main__":
    print("=" * 60)
    print("🎙️ TRỢ LÝ ẢO GIỌNG NÓI TIẾNG VIỆT LỚP 7 🎙️")
    print("=" * 60)
    
    noi_tieng_viet("Xin chào bạn! Tôi là trợ lý ảo Python lớp 7.")
    
    while True:
        cau_noi = input("\nNhập câu hỏi (hoặc gõ 'thoat' để dừng): ")
        if cau_noi.lower().strip() in ["thoat", "exit"]:
            noi_tieng_viet("Tạm biệt bạn nhé, chúc bạn một ngày vui vẻ!")
            break
            
        if "mấy giờ" in cau_noi:
            import datetime
            gio = datetime.datetime.now().strftime("%H giờ %M phút")
            noi_tieng_viet(f"Bây giờ là {gio} rồi bạn nhé.")
        else:
            noi_tieng_viet(f"Tôi đã nghe bạn nói: {cau_noi}")

# ----------------------------------------------------
# 📝 HƯỚNG DẪN CÀI ĐẶT THƯ VIỆN ÂM THANH CHO HỌC SINH:
# Chạy lệnh trong terminal:
# pip install gTTS pygame pyttsx3 SpeechRecognition
# ----------------------------------------------------
