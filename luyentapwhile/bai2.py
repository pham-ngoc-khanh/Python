# Bài 2: Nhập vào số nguyên dương n từ bàn phím. Tính và in ra n! (giai thừa của n).
# Sử dụng vòng lặp while.

import sys
import io

# Đảm bảo in ra tiếng Việt đúng định dạng trong terminal
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Nhập số n từ bàn phím
try:
    n = int(input("Nhập vào số nguyên dương n: "))
    
    if n < 0:
        print("Vui lòng nhập số nguyên dương!")
    else:
        # Tính giai thừa
        giai_thua = 1
        i = 1
        
        while i <= n:
            giai_thua *= i
            i += 1
            
        print(f"{n}! = {giai_thua}")
except ValueError:
    print("Vui lòng nhập một số nguyên!")
