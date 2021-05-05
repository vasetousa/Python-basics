a = float(input()) # real number for convertion
b = (input())  # input measure unit
c = (input())  # exit measure unit

result = 0

if b == "m" and c == "mm":
    result = a * 1000

elif b == "mm" and c == "m":
    result = a / 1000

elif b == "m" and c == "cm":
    result = a * 100

elif b == "mm" and c == "cm":
    result = a / 10

elif b == "cm" and c == "m":
    result = a / 100

elif b == "cm" and c == "mm":
    result = a * 10

print(f"{result:.3f}")