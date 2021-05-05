import math
record = float(input())  # record time in seconds
length = float(input())  # length of the distance to swim in meters
timess = float(input())  # time in seconds to swim 1m


delay = math.floor(length / 15) * 12.5  # delay while swimming (every 15m with 12.5 sec)
total_swim_time = length * timess  # total swim time
total_time = total_swim_time + delay

if total_time < record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")


else:
    result = total_time - record
    print(f"No, he failed! He was {result:.2f} seconds slower.")
