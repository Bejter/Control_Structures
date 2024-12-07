# Function to determine the quarter of the year based on the month number
def get_quarter(month):
    if month in [1, 2, 3]:
        return "Q1"
    elif month in [4, 5, 6]:
        return "Q2"
    elif month in [7, 8, 9]:
        return "Q3"
    elif month in [10, 11, 12]:
        return "Q4"
    else:
        return "Invalid month number. Please enter a number between 1 and 12."

# Test the program with the given months
test_months = [12, 10, 9, 1]

for month in test_months:
    quarter = get_quarter(month)
    print(f"Month {month} is in {quarter}.")

