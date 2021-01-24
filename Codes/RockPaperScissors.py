import os
import random
from icecream import ic
os.system('clear')

symbols = ["rock", "paper", "scissors"]

for x in range(100):  
    computerchoice = random.choice(symbols)

    choice = input("WASSUP! THIS IS ROCK, PAPER, SCISSORS!!! Choose Rock👊, Paper✋ or Scissors✌️: ").lower().strip()
    print("I did", computerchoice)
    
    if computerchoice == "rock" and choice == "paper":
        print("OH NO!! YOU WON!!")
    elif computerchoice == "rock" and choice == "scissors":
        print("TAKE THAT!! YOU LOST!!!!")

    elif computerchoice == "paper" and choice == "scissors":
        print("OH NO!! YOU WON!!")
    elif computerchoice == "paper" and choice == "rock":
        print("TAKE THAT!! YOU LOST!!!!")

    elif computerchoice == "scissors" and choice == "rock":
        print("OH NO!! YOU WON!!")
    elif computerchoice == "scissors" and choice == "paper":
        print("TAKE THAT!! YOU LOST!!!!")

    elif computerchoice == choice:
        print("TIE?!?!?! How did you do that? 🤔🤔🤔 I thought I was going to annihilate you!")
    else:
        print(f"[COMMAND NOT FOUND], what is {choice}? huh? Like WHAT IS THAT WORD?")

