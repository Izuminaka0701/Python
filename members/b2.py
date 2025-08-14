import math 

xA = float(input("Nhập tọa độ xA: "))
yA = float(input("Nhập tọa độ yA: "))
xB = float(input("Nhập tọa độ xB: "))
yB = float(input("Nhập tọa độ yB: "))
d = math.sqrt((xB - xA) ** 2 + (yB - yA) ** 2)
print("Khoảng cách giữa hai điểm A và B là: ", abs(d))