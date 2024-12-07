# Basic salary
basic_salary = 5000

# Bonus percentages
bonus_percentage = [0, 30]  # 0% and 30%

# Calculate total salary for each bonus percentage
for bonus in bonus_percentage:
    total_salary = basic_salary + (basic_salary * bonus / 100)
    print(f"Bonus: {bonus}% => Total salary: {total_salary} PLN")
