#Rock, Paper, Scissors 
#June 28, 2024
import random
import os
import time

clear = lambda: os.system('cls')

def get_user_choice():
    print("Welcome, you're about to play Rock, Paper and Scissors.")
    print("Please, choose what do ya want:\n Rock\n Paper\n Scissors")
    opc = input("Enter your option: ").lower()
    while opc not in ["rock", "paper", "scissors"]:
        clear()
        print("Not valid option")
        print("Please, choose what do ya want:\n Rock\n Paper\n Scissors")
        opc = input("Enter your option: ").lower()
    return opc 

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a Tie")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or  \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You loose!")

def opponent_choice():
    rps = ["rock", "paper", "scissors"]
    return random.choice(rps)
  

def play():
    user_choice = get_user_choice()
    computer_choice = opponent_choice()
    clear()
    print(f"You choose {user_choice}")
    print(f"Your opponent choose {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

play()