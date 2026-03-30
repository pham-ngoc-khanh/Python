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
    """
    normalized = normalize_text(exercise_description)
    
    if re.search(r"bai\s*1", normalized):
        return "Bai1.py", """# Bài 1: Viết chương trình nhập vào một số nguyên dương và in "Đây là một số chẵn" nếu nó chẵn và in "Đây là một số lẻ" nếu là số lẻ.
def main():
    try:
        n = int(input("Nhập vào một số nguyên dương: "))
        if n > 0:
            if n % 2 == 0:
                print("Đây là một số chẵn")
            else:
                print("Đây là một số lẻ")
        else:
            print("Vui lòng nhập một số nguyên dương.")
    except ValueError:
        print("Dữ liệu không hợp lệ.")

if __name__ == "__main__":
    main()
"""
    elif re.search(r"bai\s*2", normalized):
        return "Bai2.py", """# Bài 2: Nhập vào 3 số nguyên dương _a, _b, _c và in "Độ dài ba canh tam giác" nếu nó thỏa mãn.
def main():
    try:
        a = int(input("Nhập _a: "))
        b = int(input("Nhập _b: "))
        c = int(input("Nhập _c: "))
        if a > 0 and b > 0 and c > 0:
            if (a + b > c) and (a + c > b) and (b + c > a):
                print("Độ dài ba canh tam giác")
            else:
                print("Đây không phải độ dài ba canh tam giác")
        else:
            print("Vui lòng nhập số dương.")
    except ValueError:
        print("Dữ liệu không hợp lệ.")

if __name__ == "__main__":
    main()
"""
    elif re.search(r"bai\s*3", normalized):
        return "Bai3.py", """# Bài 3: Viết chương trình nhập vào năm sinh, in ra tuổi.
import time
def main():
    try:
        nam_sinh = int(input("Nhập năm sinh: "))
        year = time.localtime()[0]
        tuoi = year - nam_sinh
        if tuoi >= 0:
            print(f"Năm sinh {nam_sinh}, vậy bạn {tuoi} tuổi.")
        else:
            print("Năm sinh không hợp lệ.")
    except ValueError:
        print("Dữ liệu không hợp lệ.")

if __name__ == "__main__":
    main()
"""
    elif re.search(r"bai\s*4", normalized):
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
    
    # 2. Luôn lưu vào thư mục 3.3
    target_dir = "3.3"
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # Đường dẫn đầy đủ của file
    file_path = os.path.join(target_dir, filename)
    
    # 3. Lưu vào tệp
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code_content)
    print(f"Đã lưu tệp: {file_path}")

    # 4. Đẩy lên GitHub
    print("Đang chuẩn bị đẩy lên GitHub...")
    push_to_github(f"Tự động thêm {filename} vào {target_dir} giải đề bài: {description[:30]}")

if __name__ == "__main__":
    print("--- Chương trình Tự động Giải và Đẩy Code lên GitHub ---")
    de_bai = input("Nhập đề bài (hoặc dán văn bản): ")
    if de_bai.strip():
        process_exercise(de_bai)
    else:
        print("Vui lòng nhập đề bài.")
