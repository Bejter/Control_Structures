# Speed limit in km/h
speed_limit = 140

# Get the speed of the car from the user
car_speed = float(input("Enter the speed of the car in km/h: "))

# Check if the car exceeded the speed limit
if car_speed > speed_limit:
    print("Warning: You exceeded the speed limit!")
else:
    print("You are within the speed limit.")
