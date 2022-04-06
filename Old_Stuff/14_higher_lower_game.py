import random
import subprocess as s
import extras.higher_lower as extras

DATA = extras.data


def compare(a, b):
    if a > b:
        return "a"
    else:
        return "b"


def pick_one():
    cur = random.sample(DATA, 2)
    return cur


def game():
    score = 0
    gameover = False
    while not gameover:
        current = pick_one()
        s.call("clear")
        print(extras.logo)

        if score != 0:
            print(f"You're right! Current score: {score}")

        print(f"Compare A: {current[0]['name']}, a {current[0]['description']}, from {current[0]['country']}.")
        print(extras.vs)
        print(f"Against B: {current[1]['name']}, a {current[1]['description']}, from {current[1]['country']}.")

        answer = compare(current[0]['follower_count'], current[1]['follower_count'], )
        players_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        # print(answer, players_choice)  # debug

        if players_choice == answer:
            score += 1
        else:
            gameover = True
            s.call("clear")
            print(extras.logo)
            print(f"Sorry, that's wrong. Final score: {score}")


game()
