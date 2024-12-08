'''for i in range(6):
    print('Practice makes perfect!')

###
# Prints the name of university where you are studying
# with an extra space between characters (add a space between
# each character), e.g.
# 'book' -> 'b o o k'
#
university = 'Krakow University of Economics'
university_expanded = ''
x = 0

for char in university:
    university_expanded = university_expanded + ' ' + university[x]
    x += 1

print(university) # original university name
print(university_expanded) # expanded university name

###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''
z = 0
for char in plain_text:
    y = ord(plain_text[z])
    # read the character's code (use ord())
    if y != 32:
        y += 1
    # add one to the character's code
    t = chr(y)
    # replace new character code with its
    # corresponding character (use chr())
    encrypted_text = encrypted_text + t
    # add encrypted character to encrypted text
    z += 1
    

print(plain_text)
print(encrypted_text)

###
# Calculates the sum of integer numbers in the range <1,5>
#
sum = 0

for i in range(5,11):
    sum = sum + i

print(f'Sum is {sum}')

###
# Calculates the sum of even numbers in the range <1,10>
#
sum = 0

for i in range(1, 11):
    if not i % 2 == 0:
        continue
    sum += i

print(f'Sum of even numbers in the range <1,10> is {sum}')
'''
###
# Calculates values for the following fractions: 1/2, 1/3, ..., 1/10
#
for i in range(1,11):
    print(f'1/{i} = {1/i}')