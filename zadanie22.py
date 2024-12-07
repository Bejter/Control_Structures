# Prompt the user to enter a clothing size symbol
size_symbol = input("Enter a clothing size (S, M, L, XL): ").strip().upper()

# Check the entered symbol and print the corresponding description
if size_symbol == "S":
    print("Small size")
elif size_symbol == "M":
    print("Medium size")
elif size_symbol == "L":
    print("Large size")
elif size_symbol == "XL":
    print("Extra large size")
else:
    print("Incorrect symbol")
