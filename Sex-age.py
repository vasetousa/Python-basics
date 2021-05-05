age = float(input())
sexx = str(input())


# check and print for age and sex
if sexx == "m":
    if age >= 16:
        print("Mr.")
    else: print("Master")

if sexx == "f":
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")