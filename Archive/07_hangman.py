import random as r
import hangman.art as art
import hangman.wordlist as words
import os

print(art.logo)

chosen_word = r.choice(words.word_list)
lives = 6
end_of_game = False
display = []
guessed_letters = []

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# preparations
for i in range(len(chosen_word)):
    display.append("_")

# actual game
while not end_of_game:
    guess = input("Please, input letter: ").lower()

    # check guessed letter
    if guess not in guessed_letters:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
        guessed_letters.append(guess)
    else:
        print("You've already guessed this one")

    # output current results
    print(' '.join(display))
    print(art.stages[lives])
    if lives == 0:
        end_of_game = True
        print("You've lose!!")
    if "_" not in display:
        end_of_game = True
        print("You've won!")