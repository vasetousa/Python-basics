budget = float(input()) # film budget
decor = budget * 0.10  # decor price is 10% from the budget
extras = int(input())
price_outfit = float(input())  # extras 1 x outfit price
if extras > 150:
    price_outfit = price_outfit * 0.90
total1 = extras * price_outfit  # total money for outfits for the extras

expences = decor + total1 # total expences for the film

total2 = expences - budget  # calculate if enough money to start production
total3 = budget - expences  # calculate money left to start production

if expences > budget:  # check if the budget is enough to start the movie
    print(f"Not enough money!")
    print(f"Wingard needs {total2:.2f} leva more.")

else:
    print("Action!")
    print(f"Wingard starts filming with {total3:.2f} leva left.")




