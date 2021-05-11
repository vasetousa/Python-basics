low = 1
high = 1000
guesses = 1
print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start ")

guess = 1
while not low == high:
    # print("\tGuessing in  the range of {} to {}".format(low, high))
    # for checking the code
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h or l, or c if my guess is correct "
                     .format(guess)).casefold()

    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than
        # the guess.
        low = guess + 1
    elif high_low == "l":
        # guess lower. The high end of the range becomes 1 less than
        # the guess
        high = guess - 1
    elif high_low == "c":
        print("I've got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c")
    guesses += 1
else:
    print(f"You thought of the number {low}")
    print("I've got it in {} guesses!".format(guesses))