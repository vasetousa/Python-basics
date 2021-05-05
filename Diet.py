strob_lv = float(input("Price stroberies lv: "))  # iagodi

rasp_lv = strob_lv / 2
banana_lv = rasp_lv - rasp_lv * 0.8
orange_lv = rasp_lv - rasp_lv * 0.4

banana_kg = float(input("Bananas kg: "))
orange_kg = float(input("Oranges kg: "))
rasp_kg = float(input("Rasberies kg: "))  # malini
strob_kg = float(input("Stroberies kg: "))

total_lv = (strob_kg * strob_lv) + (banana_kg * banana_lv) + (orange_kg * orange_lv) + (rasp_kg * rasp_lv)

a = "Total amount Maria needs for the purchase: "
b = str(total_lv)
print(a + b)
