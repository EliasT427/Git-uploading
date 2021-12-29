from random import randint, random
random_numbers = [randint(0,1000) for num in range(15)]
print(random_numbers)
user_input = int(input('guess a number between 0 and 1000 '))
if user_input in random_numbers:
    print('you guessed a number')
else:
    print('you are horrible at guessing')