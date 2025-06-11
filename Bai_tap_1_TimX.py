import math

a = int(input("Nhập hệ số a: "))
b = int(input("Nhập hệ số b: "))
c = int(input("Nhập hệ số c: "))

if a != 0:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Nghiệm kép: x = {x}")
    else:
        print("Phương trình vô nghiệm trong tập số thực")
elif b != 0:
    x = -c / b
    print(f"Nghiệm của phương trình bậc nhất: x = {x}")
elif c != 0:
    print("Phương trình vô nghiệm")
else:
    print("Phương trình vô số nghiệm")
