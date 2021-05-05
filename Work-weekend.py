day = input()

# check and print if the day is working or not, also if it is a neither one (Error)
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    print("Working day")

elif day == "Saturday" or day == "Sunday":
    print("Weekend")

else:
    print("Error")


