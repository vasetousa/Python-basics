v = float(input("price 1 kg vegetables: "))
f = float(input("price 1 kg fruits: "))
va = float(input("kg vegetables: "))
fa = float(input("kg fruits: "))

price_v = (v * va) + (f * fa)

pr_euro = price_v / 1.94

print(f"{pr_euro:.2f}")

