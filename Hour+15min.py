time_h = int(input())
time_m = int(input())

min = time_m + 15  # time after 15 mins.
hour = 0  # hour is 0 for the printing to be correct
flag = 0  # flag showing if any other check had been executed, except the last one.


if time_h < 23 and min < 60:
    flag = 1
    print(f"{time_h}:{min}")

if time_h == 23 and min > 59:
    hour = 0
    flag = 1
    if abs(min - 60) < 10:
        print(f"{hour}:0{abs(min - 60)}")
    else:
        print(f"{hour}:{abs(min - 60)}")

if time_h < 23 and min > 59:
    hour = time_h + 1
    flag = 1
    if abs(min - 60) < 10:
        print(f"{hour}:0{abs(min - 60)}")
    else:
        print(f"{hour}:{abs(min - 60)}")

if time_h == 23 and time_m == 0:
    flag = 1
    print(f"{time_h}:{min}")

if time_m < 45 and flag == 0:
    print(f"{time_h}:{min}")
