import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

chuoi = input("Nhập vào một chuỗi ký tự: ")
print("Chuỗi bạn vừa nhập là:", chuoi)
