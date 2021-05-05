r_1 = int(input())
r_2 = int(input())
r_3 = int(input())

time_r = r_1 + r_2 + r_3

minuti = time_r // 60 #t he floor division // rounds the result down to the nearest whole number
secundi = time_r % 60 # modul left -> 51 / 2 = 25. modul = 1

if secundi < 10:
    print(f"{minuti}:0{secundi}")
else:
    print(f"{minuti}:{secundi}")


