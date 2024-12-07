# Employee's basic salary
basic_salary = 5000

# Ask the user for the bonus percentage
bonus_percentage = float(input("Enter the bonus percentage: "))

# Check if the bonus percentage is valid (greater than or equal to 0)
if bonus_percentage >= 0:
    # Calculate the bonus
    bonus = (basic_salary * bonus_percentage) / 100
    # Calculate the total salary
    total_salary = basic_salary + bonus
    print(f"The total salary is: {total_salary} PLN")
else:
    print("Invalid input. The bonus percentage cannot be negative.")
