# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

# ASK FOR A USER INPUT
# source: python.org
#s = input('--> ')

x = input("Please choose one of 'rock', 'paper', scissors': ")
print(x)

# VALIDATE THE USER INPUT

# if x == "rock": # "paper" "scissors"
#     print("VALID")
# else:
#     print("OOPS, INVALID, PLEASE TRY AGAIN")
#     exit()


if (x == "rock") or (x == "paper") or (x == "scissors") or (x == "ROCK") or (x == "Rock") or (x == "Paper") or (x == "PAPER") or (x == "Scissors") or (x == "SCISSORS"):
    print("VALID")
else:
    print("OOPS, INVALID ENTRY, PLEASE TRY AGAIN!")
    exit()

# print("LATER MESSAGES")

print("USER CHOSE:", x)

# GENERATE A COMPUTER CHOICE

valid_options = ["rock", "paper", "scissors"] # this is a list

c = random.choice(valid_options)

print("COMPUTER CHOSE:", c)
# print(random.choice(valid_options))

# Winner
# Source: https://realpython.com/python-rock-paper-scissors/


if x == c:
    print("Both players selected {x}. It's a tie!")
elif (x == "rock") or (x == "ROCK") or (x == "Rock"):
    if c == "scissors":
        print("Rock smashes scissors! You win!")
    else:
            print("Paper covers rock! You lose.")
elif (x == "paper") or (x == "PAPER") or (x == "Paper"):
    if c == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif (x == "scissors") or (x == "SCISSORS") or (x == "Scissors"):
    if c == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

print("Thank You For Participating In Our Game!!!")
print("Please Play Again!")
