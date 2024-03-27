

# Generate a random number in python and gess that randomly generated number :


import random

number = random.randint(0,10)

guess = int(input("Enter your guessed number:"))
#print("randomly generated number:",number)

while number != guess:
    if guess <number:
        print("guess is too low")
        guess = int(input("Enter your guess number again:"))
    elif (guess > number):
        print("guess is too high")
        guess= int(input("Enter your guess number again:"))
    else:
        break;

print("your guess is correct")
