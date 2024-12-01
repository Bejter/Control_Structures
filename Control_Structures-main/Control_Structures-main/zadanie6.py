#2
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0

i = 0

while i < len(text):
    if text[i] in vowels:
        vowel_count += 1
    i+=1

print(f"The number of vowels in the text is: {vowel_count}")

#3

light_switch1 = False 
light_switch2 = False
bulbs_on = 0
if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 2
print(f'Light bulbs on: {bulbs_on}')

#4

new_password = input('Enter new password: ')
if len(new_password) < 12:
   print('Password too short (min. 12 chars)') 

#5

temperature = 33
if temperature > 35:
    print("It's extremly hot")
elif temperature > 30:
    print("It's hot")
elif temperature >= 15:
    print("It's warm")
elif temperature >= 0:
    print("It's cold")
elif temperature < 0:
    print("Warning, frost!")

#6

hourSpentInParking = int(input("Enter how many hours you spent in parkinglot"))
if hourSpentInParking == 1 or hourSpentInParking == 2:
    print("You need to pay 5 PLN")
elif hourSpentInParking >= 3 or hourSpentInParking <= 6:
    print("You need to pay 15 PLN")
elif hourSpentInParking > 6:
    print("You need to pay 20 PLN ")

#7

age = int(input("Enter your age"))
if age > 0:
    if age < 13:
        print("Child group")
    elif age <= 19:
        print("Teen group")
    elif age <= 64:
        print("Adult group")
    else:
        print("Senior group")

#8

person1_name = input('Enter first person name: ')
person1_age = int(input('Enter first person age: '))
person2_name = input('Enter second person name: ')
person2_age = int(input('Enter second person age: '))
if person1_age >= 18 and person2_age >= 18:
    print(f'Both {person1_name} and {person2_name} are adults')
else:
    print(f'Either {person1_name} or {person2_name} is not an adult')

#9

name = input("Enter your name:")
name_length = len(name)
if name[name_length - 1] == 'a':
    print("Polish female name")

#10

dogAgeInHuman = int(input("Enter the dogs age in human years: "))
dogAgeInDog = 0
for i in range(dogAgeInHuman):
    if i < 2:
        dogAgeInDog += 10.5
    else:
        dogAgeInDog += 4

print(f"The dog's age in dog's years is {dogAgeInDog}")

#11

currentPrice = float(input("Enter current price: "))
previousPrice = float(input("Enter previous price: "))

priceReducePercentage = (previousPrice - currentPrice) / previousPrice * 100

if priceReducePercentage >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {priceReducePercentage}%")

#12

productNumbers = int(input("Enter numbers of products purchased: "))
productPrice = float(input("Enter product price: "))

priceTotal = 0

for i in range(productNumbers):
    if(i <= 2):
        priceTotal += productPrice
    else:
        priceTotal += productPrice/4

print(f"Amount to pay: {productPrice}")

#13

car_speed = int(input("Enter car speed: "))
speed_limit_min = 40
speed_limit_max = 140

if car_speed < 40 and speed_limit_max > 140:
    print("Warning: invalid car speed!!")

#14

facebook = True
twitter = False
instagram = True

if facebook == True and twitter == True or facebook == True and instagram == True or twitter == True and instagram == True:
    print("You are a good influencer!")
else:
    print("You are the worst influencer I've ever seen")

#15

EAN_13_number = input("Enter EAN-13 article number: ")

if EAN_13_number.isdigit():
    if len(EAN_13_number) == 13:
        print("Article number is correct")
        if EAN_13_number[0:3] == "590":
            print(EAN_13_number[0:3])
            print("Article manufactured in Poland")
    else:
        print("Article number is not correct")
else:
    print("Article number must contain only numbers")

#16

total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:')
extra_rinse = input('Extra rinse? (y/n)')
extra_spin = input('Extra spin? (y/n)')

rinse = False
spin = False
washing_product = ""

if program == 'j':
    total_washing_time += 40
    washing_product = "Jacket"
elif program == 'u':
    total_washing_time += 70
    washing_product = "Underwear"
else:
    total_washing_time += 20
    washing_product = "Shoes"

if extra_rinse == 'y':
    total_washing_time += 15
    rinse = True

if extra_spin == 'y':
    total_washing_time += 9
    spin = True

print(f"Washing product: {washing_product}")
print(f"rinse: {rinse}")
print(f"spin: {spin}")
print(f"Total washing time: {total_washing_time} minutes")

#17

timeIn24HFormat = input("Enter time in 24-hour format: (hh:mm)")

amOrPm = "am"

hour = timeIn24HFormat[0:2]
if ":" in hour:
    hour = int(hour[0])
    minute = int(timeIn24HFormat[2:4])
else:
    minute = int(timeIn24HFormat[3:5])
    hour = int(timeIn24HFormat[0:2])

if hour > 12:
    hour12Format = hour - 12
    amOrPm = "pm"
else:
    hour12Format = hour
    amOrPm = "am"

print(f"Time in 12-hour format: {hour12Format}:{minute}{amOrPm}")

#18

x = input("Enter x: ")
y = input("Enter y: ")

if x > 0 and y > 0:
    print("Point is located at 1 quadrant")
elif x < 0 and y > 0:
    print("Point is located in 2 quadrant")
elif x < 0 and y < 0:
    print("Point is located in 3 quadrant")
elif x > 0 and y < 0:
    print("Point is located in 4 quadrant")
elif x == 0 and y == 0:
    print("Point is located on position (0,0)")
elif x == 0:
    print("Point is located on X axis")
elif y == 0:
    print("Point is located on Y axis")

#19

print("SURVEY")
computerScience = input("Are you interested in computer science? (y/n)")
computerGames = input("Do you like playing computer games? (y/n)")
instagramAcc = input("Do you have an Instagram account? (y/n)")

if computerScience == 'y':
    computerScience = True
else:
    computerScience = False

if computerGames == 'y':
    computerGames = True
else:
    computerGames = False

if instagramAcc == 'y':
    instagramAcc = True
else:
    instagramAcc = False

print("SURVEY RESULTS")
print(f"Interested in computer science: {'yes' if computerScience == True else 'no'}")
print(f"Interested in computer games: {'yes' if computerGames == True else 'no'}")
print(f"Have an instagram account: {'yes' if instagramAcc == True else 'no'}")

#20

decimal_num = int(input("Enter decimal number: "))  

binary_num = ""  

while decimal_num > 0:
    remainder = decimal_num % 2
    binary_num = str(remainder) + binary_num  
    decimal_num = decimal_num // 2  

print(f"{decimal_num}(10) = {binary_num}(2)")

#21

amount = int(input("Enter amount of polish zloty: "))

count5 = 0
count2 = 0
count1 = 0

while amount > 0:
    if amount >= 5:
        amount -= 5
        count5 += 1 
    elif amount >= 2:
        amount -= 2
        count2 += 1
    elif amount >= 1:
        amount -= 1
        count1 += 1


print(f"{amount} polish zloty is: {count5} - 5 zloty, {count2} - 2 zloty, {count1} - 1 zloty")

#22

for i in range(1, 30):
    if i%5 == 0 and i%3 == 0:
        print("both")
    elif i%5 == 0:
        print("FIVE")
    elif i%3 == 0:
        print("Three")
    else:
        print(i)

#23

number = int(input("Enter number: "))

for i in range(1,11):
    print(f"{number} x {i} = {number * i}")

#24

licznik = 1
for i in range(1,10):
    if i < 5:
        print("*" * licznik)
        licznik += 1
    else:
        print("*" * licznik)
        licznik -= 1

#25

for i in range(1,10):
    print(f"{i}" * i)

#26

attemps = 1
pin_code = 1928


