salary = float(input("Enter your monthly salary: "))
salary_quarter = (salary*3)
percent_1 = 0.18
military_1 = 0.015
social_1 = 0.22
total_taxation = (salary_quarter*(percent_1+military_1+social_1))
print("Total taxes for 3 months fiscal period: $", (total_taxation))
