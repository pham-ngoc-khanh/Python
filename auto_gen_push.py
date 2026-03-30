import os
import subprocess
from auto_push import push_to_github

import re

def normalize_text(text):
    # Chuyển về chữ thường, bỏ dấu cơ bản để so sánh (đơn giản hóa)
    text = text.lower()
    # Thay thế các ký tự có dấu phổ biến (có thể mở rộng thêm)
    replacements = {
        'à': 'a', 'á': 'a', 'ả': 'a', 'ã': 'a', 'ạ': 'a',
        'è': 'e', 'é': 'e', 'ẻ': 'e', 'ẽ': 'e', 'ẹ': 'e',
        'ì': 'i', 'í': 'i', 'ỉ': 'i', 'ĩ': 'i', 'ị': 'i',
        'ò': 'o', 'ó': 'o', 'ỏ': 'o', 'õ': 'o', 'ọ': 'o',
        'ù': 'u', 'ú': 'u', 'ủ': 'u', 'ũ': 'u', 'ụ': 'u',
        'đ': 'd'
    }
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    return text

def generate_code_placeholder(exercise_description):
    """
    Hàm này trong thực tế sẽ gọi AI API (OpenAI, Gemini, v.v.)
    Để giải quyết đề bài đã cho.
    Dưới đây là giả lập cho Bài 4 và Bài 5.
    """
    normalized = normalize_text(exercise_description)
    
    if re.search(r"bai\s*4", normalized):
        return "Bai4.py", """# Bài 4: Viết chương trình nhập một số nguyên dương và kiểm tra xem số đó có chia hết cho 2 hoặc cho 3 hoặc cả hai hay không?

def main():
    try:
        n = int(input("Nhập một số nguyên dương: "))
        if n <= 0:
            print("Vui lòng nhập một số nguyên dương.")
            return

        if n % 2 == 0 and n % 3 == 0:
            print(f"{n} chia hết cho cả 2 và 3.")
        elif n % 2 == 0:
            print(f"{n} chia hết cho 2.")
        elif n % 3 == 0:
            print(f"{n} chia hết cho 3.")
        else:
            print(f"{n} không chia hết cho 2 cũng không chia hết cho 3.")
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên.")

if __name__ == "__main__":
    main()
"""
    elif re.search(r"bai\s*5", normalized):
        return "Bai5.py", """# Bài 5: Viết chương trình giải phương trình bậc 2: a*x*x + b*x + c = 0.
import math

def main():
    try:
        a = float(input("Nhập a: "))
        b = float(input("Nhập b: "))
        c = float(input("Nhập c: "))
        
        if a == 0:
            if b == 0:
                print("Phương trình vô nghiệm" if c != 0 else "Phương trình vô số nghiệm")
            else:
                print(f"Nghiệm: x = {-c/b}")
            return

        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            print(f"Nghiệm: x1 = {x1}, x2 = {x2}")
        elif delta == 0:
            print(f"Nghiệm kép: x = {-b/(2*a)}")
        else:
            print("Phương trình vô nghiệm thực.")
    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    main()
"""
    else:
        # Nếu không phải bài 4 hoặc 5, trả về một tệp mẫu
        return "Bai_Moi.py", "# Đề bài: " + exercise_description + "\n\nprint('Chưa có logic cho bài này.')"

def process_exercise(description):
    print(f"\nĐang xử lý đề bài: {description[:50]}...")
    
    # 1. Tạo mã nguồn từ đề bài
    filename, code_content = generate_code_placeholder(description)
    
    # 2. Lưu vào tệp
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code_content)
    print(f"Đã lưu tệp: {filename}")

    # 3. Đẩy lên GitHub
    print("Đang chuẩn bị đẩy lên GitHub...")
    push_to_github(f"Tự động thêm {filename} giải đề bài: {description[:30]}")

if __name__ == "__main__":
    print("--- Chương trình Tự động Giải và Đẩy Code lên GitHub ---")
    de_bai = input("Nhập đề bài (hoặc dán văn bản): ")
    if de_bai.strip():
        process_exercise(de_bai)
    else:
        print("Vui lòng nhập đề bài.")
