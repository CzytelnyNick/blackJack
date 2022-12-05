import random
import time
import sys
import os
from game import playGame
def main():
    print("Welcome to Blackjack!")
    print("The goal of the game is to get as close to 21 as possible, without going over.")
    print("Aces count as 1 or 11, picture cards as 10, and any other card is its pip value.")
    print("You will be playing against the dealer.")
    print("The dealer will hit until he reaches 17.")
    print("Good Luck!")
    time.sleep(3)
    playAgain = "y"
    while playAgain == "y":
        playGame()
        playAgain = input("Do you want to play again? (y/n): ")
main()