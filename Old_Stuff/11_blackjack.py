from extras.blackjack import logo
import random as r
import subprocess as s

#! My_attempt(failed)

    # cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # user_deck = [r.choice(cards), r.choice(cards)]
    # computer_deck = [r.choice(cards), r.choice(cards)]
    # result_of_a_game = ""
    # game_is_not_end = True
    # s.call("clear")
    # ask_for_game = input("Do you want to play some Blackjack? y/n: ").lower()

    # if ask_for_game != "y":
    #     exit("So why you are here?")
    # s.call("clear")
    # print(logo)

    # def blackjack(deck):
    #     result = False
    #     if sum(deck) == 21:
    #         result = True
    #     return result

    # def over_21(deck):
    #     result = False
    #     if sum(deck) > 21:
    #         if 11 in deck:
    #             if sum(deck) - 10 < 21:
    #                 return result
    #             else:
    #                 result = True
    #                 return result
    #         else:
    #             result = True
    #             return result
    #     else:
    #         return result

    # while game_is_not_end:
    #     user_deck = [r.choice(cards), r.choice(cards)]
    #     computer_deck = [r.choice(cards), r.choice(cards)]
    #     if blackjack(computer_deck) == True:
    #         result_of_a_game = "lose"
    #         game_is_not_end = False
    #         print("Computer has blackjack:", computer_deck, "You are", result_of_a_game)

    #     elif blackjack(user_deck) == True:
    #         result_of_a_game = "win"
    #         game_is_not_end = False
    #         print("You have blackjack:", user_deck, "You are", result_of_a_game)

    #     elif over_21(user_deck) == True:
    #         result_of_a_game = "lose"
    #         game_is_not_end = False
    #         print("Computer deck is:", computer_deck, "\nUser deck is:", user_deck, "You are", result_of_a_game)

    #     else:
    #         print("sup")
    #         print("Computer deck is:", computer_deck, "\nUser deck is:", user_deck)
    #         game_is_not_end = False

s.call("clear")

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = r.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards an return the score calculated from the cards"""
    if sum(cards) ==21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif user_score == 0:
        return "You win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():

    user_cards = []
    computer_cards = []
    is_game_over = False
    user_score = 99
    computer_score = 99

    print(logo)
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards} current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 and computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass:\t")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final_score: {user_score}")
    print(f"    Computer's final hand : {computer_cards}, final_score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play the game of Blackjack? Type 'y' or 'n'\t") == 'y':
    s.call("clear")
    play_game()