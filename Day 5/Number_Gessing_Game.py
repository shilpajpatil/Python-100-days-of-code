


from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

# fun to check user's guess against actual answer

def check_ans(guess,answer,turns):

    if guess > answer:
        print("Too high")
        return turns-1;
    elif guess <answer:
        print("Too low")
        return turns -1
    else:
        print(f"you got it! the answer was {answer}.")

    #function to set difficulty

def set_difficulty():
    level = input("choose a difficulty.type 'easy' or 'hard':")

    if level == "easy":
        return EASY_LEVEL;
    else:
        return HARD_LEVEL


def game():
    #choosing a random number between 1 to 100
    print("Welcome to number guessing game:")
    answer = randint(1,100)
    print("correct ans {answer}" )

    turns = set_difficulty()

    guess = 0;

    while guess != answer:
        print(f"you have {turns} attempt remaining to guess the number")

        # let the user guess number
        guess =int(input("Make the guess:"))

        turns = check_ans(guess,answer,turns)
        if turns==0:
            print("you.ve run out of guess,you lose")
            return
        elif guess != answer:
            print("guess again")

game()










