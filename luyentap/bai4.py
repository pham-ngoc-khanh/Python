import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

s1 = input("Nhập chuỗi thứ nhất: ")
s2 = input("Nhập chuỗi thứ hai: ")
s3 = input("Nhập chuỗi thứ ba: ")

ket_qua = f"{s1} {s2} {s3}"
print("Chuỗi sau khi ghép là:", ket_qua)
