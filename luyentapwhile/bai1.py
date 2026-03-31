import sys
import io

# Đảm bảo in ra tiếng Việt đúng định dạng trong terminal
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Bài 1: Tính và in ra tích của 10 số tự nhiên đầu tiên.
# Sử dụng vòng lặp while.

# Giả định 10 số tự nhiên đầu tiên để tính tích là 1, 2, ..., 10 
# (Vì nếu tính từ 0 thì tích sẽ bằng 0)

i = 1
tich = 1

while i <= 10:
    tich *= i
    i += 1

print(f"Tích của 10 số tự nhiên đầu tiên là: {tich}")
