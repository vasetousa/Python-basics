    deposit = float(input("Deposit amount: "))
    period_months = int(input("How many months: "))
    interest = float(input("Interest rate %: ")) / 100

    # сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
    # amount = deposited amount + term of the deposit * (deposited amount * annual interest rate) / 12)

    result = deposit + period_months * ((deposit * interest) / 12)  # calculate the result
    a = "Total amount + interest: "
    b = str(result)  # this number as text
    c = result - deposit  # interest
    e = str(c)  # interest as text
    d = "Total interest: "
    print(a + b)  # print text + text
    print(d + e)  # print text + text
