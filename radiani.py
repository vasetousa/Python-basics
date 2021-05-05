# import lib
# from math import pi - deg = rad * 180 / pi
# import math - deg = rad * 180 / math.pi

import math

rad = float(input())
# degrees = radians * 180 / pi (3.1415729)
deg = rad * 180 / math.pi

# floor - round the number to the lesser one - 1.63 -> 1
# print(math.floor(1.63)) -> 1
# ceil - round the number to the higher one - 1.63 -> 2
# print(math.ceil(1.63)) -> 2 , math.ceil(1.13) -> 2
# print(f"{1.13:.0f}") -> 1

print(math.floor(deg))
