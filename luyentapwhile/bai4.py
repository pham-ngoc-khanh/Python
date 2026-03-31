# Bài 4: Nhập vào từ bàn phím số nguyên n.
# In ra tổng của các số thỏa mãn hai điều kiện: nhỏ hơn n và là số chẵn.
# Sử dụng vòng lặp while.

import sys
import io

# Đảm bảo in ra tiếng Việt đúng định dạng trong terminal
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

try:
    n = int(input("Nhập vào số nguyên n: "))
    
    tong = 0
    # Giả sử chúng ta xét các số từ 0 (hoặc số âm nếu n âm, 
    # nhưng thường bài tập này ám chỉ các số không âm nhỏ hơn n)
    # Ở đây tôi sẽ tính tổng các số chẵn không âm nhỏ hơn n.
    # Nếu n là số âm, tổng sẽ là 0.
    
    i = 0
    while i < n:
        if i % 2 == 0:
            tong += i
        i += 1
        
    print(f"Tổng các số chẵn nhỏ hơn {n} là: {tong}")
except ValueError:
    print("Vui lòng nhập một số nguyên!")
