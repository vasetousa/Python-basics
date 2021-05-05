from math import floor

income = float(input())  # income in BGN
average_score = float(input())  # average score in school
min_salary = float(input())  # min salary in the country

soc_scolarship = 0
excell_scolarship = 0

if average_score > 4.50 and income < min_salary:
    soc_scolarship = floor(min_salary * 0.35)

if average_score >= 5.50:
    excell_scolarship = floor(average_score * 25)

if soc_scolarship == 0 and excell_scolarship == 0:
    print("You cannot get a scholarship!")
elif soc_scolarship != 0 and excell_scolarship == 0:
    print(f"You get a Social scholarship {soc_scolarship} BGN")
elif soc_scolarship == 0 and excell_scolarship != 0:
    print(f"You get a scholarship for excellent results {excell_scolarship} BGN")

else:
    if soc_scolarship > excell_scolarship:
        print(f"You get a Social scholarship {soc_scolarship} BGN")
    elif  soc_scolarship < excell_scolarship:
        print(f"You get a scholarship for excellent results {excell_scolarship} BGN")
    else:
        print(f"You get a scholarship for excellent results {excell_scolarship} BGN")




