# Function to calculate total fuel consumption
def calculate_fuel_consumption(distance, mode):
    # Fuel consumption rates for different modes
    fuel_rates = {
        "A": 7,  # Auto mode
        "M": 9,  # Manual mode
        "E": 6   # Eco mode
    }
    
    # Check if the mode is valid
    if mode not in fuel_rates:
        return "Incorrect driving mode."
    
    # Calculate fuel consumption for the given distance and mode
    fuel_consumption = (distance / 100) * fuel_rates[mode]
    
    return fuel_consumption

# Test the program with the provided data
test_data = [
    (200, "M"),  # 200 km, Manual mode
    (400, "A"),  # 400 km, Auto mode
    (350, "E")   # 350 km, Eco mode
]

# Calculate and print the total fuel consumption for each case
for distance, mode in test_data:
    result = calculate_fuel_consumption(distance, mode)
    print(f"Distance: {distance} km, Mode: {mode} => Total fuel consumption: {result} liters")
