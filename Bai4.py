# Bài 4: Viết chương trình nhập một số nguyên dương và kiểm tra xem số đó có chia hết cho 2 hoặc cho 3 hoặc cả hai hay không?

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
