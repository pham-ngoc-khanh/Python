# Bài 3: Nhập vào số nguyên dương n từ bàn phím. Kiểm tra xem số n có phải là số nguyên tố hay không.
# Sử dụng vòng lặp while.

import sys
import io

# Đảm bảo in ra tiếng Việt đúng định dạng trong terminal
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

try:
    n = int(input("Nhập vào số nguyên dương n: "))
    
    if n < 1:
        print("Vui lòng nhập số nguyên dương!")
    elif n == 1:
        print("Không phải số nguyên tố.")
    else:
        is_prime = True
        i = 2
        
        # Kiểm tra từ 2 đến căn bậc 2 của n
        while i * i <= n:
            if n % i == 0:
                is_prime = False
                break
            i += 1
            
        if is_prime:
            print("Đây là số nguyên tố.")
        else:
            print("Không phải số nguyên tố.")
except ValueError:
    print("Vui lòng nhập một số nguyên!")
