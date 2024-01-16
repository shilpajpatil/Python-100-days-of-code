

# Virtual coint toss program


# Here I am using inbuilt random module

import random

def cointoss():
    print("virtual coin toss program")

    random_number = random.randint(0,1)
    if random_number ==1:
        print("Heads")
    elif random_number ==0:
        print("Tails")
