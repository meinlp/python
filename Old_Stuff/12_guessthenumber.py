import subprocess as s
from random import randint
from extras.guessthenumber import logo

s.call("clear")
print(logo)
print("Welcome to the Number Guessing Game.\nI'm thinking of a number between 1 and 100 and you should guess it.")

ANSWER=randint(1, 100)

#### HINT ####
# print(f"Psst, the correct answer is {ANSWER}")

DIFFICULTY=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if DIFFICULTY == 'easy':
    ATTEMPTS = 10
elif DIFFICULTY == 'hard':
    ATTEMPTS = 5
else:
    print("LOL U MAD? You've got typo, maybe")
    print(f"You've printed {DIFFICULTY}, we're end here")
    exit()

def check_choice(guess):
    if guess > ANSWER:
        result = "Too high"
    elif guess < ANSWER:
        result = "Too low"
    else:
        result = "Exact"
    return result


def play_game():
    win = False
    for i in range(ATTEMPTS):
        print(f"You have {ATTEMPTS - i} attempts remaining to guess your number")
        guess = int(input("Make a guess: "))
        result = check_choice(guess)
        if result == "Exact":
            print(f"You got it! The answer was {ANSWER}")
            win = True
            break
        else:
            print(result)
    if not win:
        print("You've run out of guesses, you lose.")

play_game()