pages = int(input("Pages Count: "))
pages_h = int(input("Pages per hour: "))
days = int(input("Days to read the book: "))

time_book = pages / pages_h
hours = time_book / days

print(hours)

