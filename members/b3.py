import math 

xC = float(input("Nhập tọa độ xC: "))
yC = float(input("Nhập tọa độ yC: "))
R = float(input("Nhập bán kính R: "))
xM= float(input("Nhập tọa độ xM: "))
yM = float(input("Nhập tọa độ yM: "))

d = math.sqrt((xC - xM) ** 2 + (yC - yM) ** 2)
if d < R:
    print("Điểm M nằm trong mặt cầu.")
elif d == R:
    print("Điểm M nằm trên mặt cầu.")
else:
    print("Điểm M nằm ngoài mặt cầu.")