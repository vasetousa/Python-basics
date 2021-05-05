l = int(input("Length: "))
w = int(input("Width: "))
h = int(input("Height: "))
o = l * w * h / 1000  # dm3

v = float(input("Volume used space %: "))   # volume used by sand, pump, heater etc

dm = o - (o * v / 100)
str = "litles"
print(dm)








