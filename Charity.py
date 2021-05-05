period = int(input("How many days for the campaign: "))
makers = int(input("How many makers: "))
cakes = int(input("How many cakes: "))
waffles = int(input("How many waffles: "))
pancakes = int(input("How many pancakes: "))

# calc total items
total_cake = cakes * period * makers * 45
total_waffle = waffles * period * makers * 5.8
total_pancake = pancakes * period * makers * 3.2
total_items = total_cake + total_waffle + total_pancake

# calc items total price
sum_all = total_cake + total_waffle + total_pancake

no_expenses = sum_all * 1 / 8
gr_total = sum_all - no_expenses
print(f"{gr_total:.2f}")
print(gr_total)