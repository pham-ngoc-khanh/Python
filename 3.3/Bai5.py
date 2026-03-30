# Bài 5: Viết chương trình giải phương trình bậc 2: a*x*x + b*x + c = 0.
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
