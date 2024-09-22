import turtle
import pandas
from pointer import Pointer

screen = turtle.Screen()
screen.title("U.S. States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pointer = Pointer()

data = pandas.read_csv("50_states.csv")
with open("highscore") as score:
    high_score = int(score.read())
correct_guesses = []
while len(correct_guesses) < 50:

    answer_state = screen.textinput("Guess the State", "What's another state's name?").title()
    if answer_state == 'Exit':
        missing_states = [state for state in data.state.to_list() if state not in correct_guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in data.state.to_list():
        guess = data[data.state == answer_state].values.tolist()
        pointer.print(guess[0])
        correct_guesses.append(guess[0][0])
        if len(correct_guesses) > high_score:
            with open('highscore', "w") as highscore:
                highscore.write(str(len(correct_guesses)))
    else:
        print(correct_guesses)
    # screen.exitonclick()
