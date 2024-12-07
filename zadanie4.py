# Function to perform the calculator operation
def calculator():
    # Ask the user to input the operation symbol
    operation = input("Enter operation (+, -, *, /): ").strip()
    
    # Ask the user to input two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Perform the operation based on user input
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                return "Error: Division by zero is not allowed."
        else:
            return "Invalid operation. Please use +, -, *, or /."
        
        return f"The result of {num1} {operation} {num2} is: {result}"
    
    except ValueError:
        return "Invalid input. Please enter valid numbers."

# Testing the calculator with the required operations
print(calculator())  # Example 1: 2 + 3
print(calculator())  # Example 2: 2 * 4
print(calculator())  # Example 3: 3 - 5
print(calculator())  # Example 4: 5 * 6
