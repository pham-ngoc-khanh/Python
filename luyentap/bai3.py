import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

a = int(input("Nhập số nguyên thứ nhất (a): "))
b = int(input("Nhập số nguyên thứ hai (b): "))
c = int(input("Nhập số nguyên thứ ba (c): "))

print(f"a) Tổng: {a + b + c}, Tích: {a * b * c}")
print(f"b) Hiệu của {a} và {b}: {a - b}")

if b != 0:
    print(f"c) Phép chia giữa {a} và {b}:")
    print(f"   - Phần nguyên: {a // b}")
    print(f"   - Phần dư: {a % b}")
    print(f"   - Kết quả chính xác: {a / b}")
else:
    print("c) Không thể chia cho 0")
