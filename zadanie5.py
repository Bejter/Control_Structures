#2

count = 0
while count < 5:
    print(count)
    count += 1

#3

name = ''

while name == '':
    name = input('Enter your name: ')

print(f'Hello {name}')

#4

import random

number_to_guess = random.randint(1, 100)
user_guess = 0

print("Guess the number between 1 and 100!")

while user_guess != number_to_guess:
    user_guess = int(input("Enter your guess: "))

    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")


#5

total_sum = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break 
    total_sum += number

print(f"The total sum of the numbers is: {total_sum}")

#6

N = 10
sum_even = 0

for i in range(1, N + 1):
    if i % 2 == 0:
        sum_even += i

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")

#7

import time

countdown = int(input("Enter the number of seconds to count down: "))

countdown_words = ["One", "Two", "Three", "Four", "Five"]

while countdown > 0:
    if countdown <= 5:
        print(countdown_words[countdown-1])
    else:
        print(countdown)
    countdown -= 1
    time.sleep(1) 

print("Time's up!")

#8

balance = 1000 
pin = '1111'

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")

    elif choice == '2':

        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")

    elif choice == '3':

        amount = float(input("Enter the amount to withdraw: "))

        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")

    elif choice == '4':

        user_pin = input("Insert PIN: ")     

        if user_pin.isdigit():
            if user_pin == pin:
                print("PIN is correct!")
            else:
                print("PIN is incorrect!")
        else:
            print("PIN must contain only digits!")

    elif choice == '5':

        user_pin = input("Insert your PIN: ")

        if user_pin.isdigit():
            if user_pin == pin:
                print("PIN is correct! Now you can change your PIN")
                new_pin = input("insert PIN: ")
                if new_pin.isdigit():
                    pin = new_pin
                    print("succesfully changed PIN")
                else:
                    print("PIN must contain only digits!")
            else:
                print("PIN is incorrect!")
        else:
            print("PIN must contain only digits!")
    
    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break  
    else:
        print("Invalid option. Please try again.")