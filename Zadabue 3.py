###
# Checking login and password
#
login = 'joe'
password = 'abcd'
entered_login = input('Login: ')
entered_password = input('Password: ')
if login == entered_login and password == entered_password :
    print('You are logged in')
else : 
    print('Incorrect login or password!!')


###
# Checking if discount is available
# The discount is available to children under 18,
# or people 65 or older.
#
age = int(input('Enter your age: '))

if age < 18 or age > 65 :
    print(f'Your age is {age}, you can get discount')
else:
    print(f'Your age is {age}, you cant get discount')
###
# Checks whether at least one number entered
# from the keyboard is not negative
# 
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

if not x < 0 or not y < 0 :
    print(f'At least one of the numbers {x} and {y} is not negative')
else :
    print(f'Both of them are negative')
###
# Calculates the number of days in a month
#
month = int(input('Enter month number (1..12)'))

if month % 2 == 1:
    days = 31 ## months with 31 days
elif month % 2 == 0 and not month == 2 :
    days = 30 ## months with 30 days
else:
    days = 28
## February 28 days 

print(f'Month {month} has {days} days')

###
# Checks if the given day number of the month is correct
#
month = int(input('Enter month number (1..12): '))
day = int(input('Enter the day number of the month: '))
day_ok = False

if month % 2 == 1 and month <= 12 and month >= 1:
    if day >=1 and day <= 31:
        day_ok = True
elif month % 2 == 0 and not month==2 and month <= 12 and month >= 1:
    if day >=1 and day <= 30:
        day_ok = True
elif month == 2 :
    if day >= 1 and day <= 28:
        day_ok = True
else:
    day_ok = False

message = f'Day {day} for the month {month}'
if day_ok:
    print(f'{message} is correct')
else:
    print(f'{message} is not correct')