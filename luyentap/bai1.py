import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
tong = a + b
print(f"Tổng của {a} và {b} là: {tong}")
