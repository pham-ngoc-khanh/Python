import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

_R = float(input("Nhập bán kính đường tròn (_R): "))
_pi = 3.14

CV = 2 * _R * _pi
DT = _pi * _R * _R

print(f"Chu vi hình tròn (CV): {CV}")
print(f"Diện tích hình tròn (DT): {DT}")
