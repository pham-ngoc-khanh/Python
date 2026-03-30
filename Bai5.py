# Bài 5: Viết chương trình giải phương trình bậc 2: a*x*x + b*x + c = 0.
# Trong đó 3 tham số a,b,c được nhập từ bàn phím.
# Sử dụng thư viện math và hàm tính căn sqrt().

import math

def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình có vô số nghiệm.")
            else:
                print("Phương trình vô nghiệm.")
        else:
            x = -c / b
            print(f"Phương trình bậc 1 có nghiệm: x = {x}")
        return

    delta = b**2 - 4*a*c
    print(f"Delta = {delta}")

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép: x = {x}")
    else:
        print("Phương trình vô nghiệm (trong tập số thực).")

def main():
    try:
        a = float(input("Nhập tham số a: "))
        b = float(input("Nhập tham số b: "))
        c = float(input("Nhập tham số c: "))
        solve_quadratic(a, b, c)
    except ValueError:
        print("Lỗi: Vui lòng nhập các tham số là số.")

if __name__ == "__main__":
    main()
