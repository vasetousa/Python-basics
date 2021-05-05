vac_price = float(input("Vacation price: "))

puzzel = int(input("Puzzel count: "))
doll = int(input("Doll count: "))
bear = int(input("Bear count: "))
minion = int(input("Minion count: "))
truck = int(input("Truck count: "))

p = puzzel * 2.6
d = doll * 3
b = bear * 4.1
m = minion * 8.2
t = truck * 2

all = puzzel + doll + bear + minion + truck  # count of toys sold
total: float = p + d + b + m + t  # count of total money made from sells

val1 = 0.0
if all >= 50:
    val1 = total * 0.75  # price after 25% discount

else:
    val1 = total

money_rest = val1 - val1 * 0.1  # Profit left after rent was paid

if money_rest >= vac_price:   # check if there is enough money for vacation
    rest = money_rest - vac_price
    print(f"Yes! {rest:.2f} lv left.")

else:
    rest = vac_price - money_rest
    print(f"Not enough money {rest:.2f} lv. needed.")
