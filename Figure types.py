area = 0
shape = input()
import math
if shape == "square":
    a = float(input())
    area = a * a


elif shape == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b


elif shape == "circle":
    r = float(input())
    area = r * r * math.pi  # also math.pow(r,2) or r ** 2


elif shape == "triangle_print":
    a = float(input())
    h = float(input())
    area = a * h / 2


print(f"{area:.3f}")


