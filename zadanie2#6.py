# Function to check if the number is positive, negative, or zero
def check_number(number):
    if number > 0:
        return f"Number {number} is positive"
    elif number < 0:
        return f"Number {number} is negative"
    else:
        return "Number is 0"

# Test the program with the given numbers
test_numbers = [7, 1, 0, -1, -4]

for number in test_numbers:
    result = check_number(number)
    print(result)
