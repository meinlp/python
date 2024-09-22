from os import name
from extras.auction_logo import logo
import subprocess

subprocess.run("clear")
print(logo)
print("Welcome to the auction, fellas!")

auctioneers = {}
show_must_go_on = True


def find_a_winner(all_auctioneers):
    highscore = ["", 0]
    for bidder in all_auctioneers:
        if all_auctioneers[bidder] > highscore[1]:
            highscore = [bidder, all_auctioneers[bidder]]
    print(f"{highscore[0]} wins today with highest bid of ${highscore[1]}")


while show_must_go_on:
    name = input("How is your name? ")
    bid = int(input(f"Place your bid, {name}: $"))
    auctioneers[name] = bid
    do_we_continue = input("Anyone else want to make a bid? Y/N ").lower()
    if do_we_continue == "n":
        show_must_go_on = False
    else:
        subprocess.run("clear")

subprocess.run("clear")
find_a_winner(auctioneers)
