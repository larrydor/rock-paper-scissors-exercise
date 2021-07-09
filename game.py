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
    print("Sorry, You have entered an Invalid Entry. PLEASE TRY AGAIN!")
    exit()

# print("LATER MESSAGES")

print("USER CHOSE:", x)

# GENERATE A COMPUTER CHOICE

valid_options = ["rock", "paper", "scissors"] # this is a list

c = random.choice(valid_options)

print("COMPUTER CHOSE:", c)
# print(random.choice(valid_options))

# Determing Winner

# Source: https://realpython.com/python-rock-paper-scissors/

if x == c:
    print("Both players selected {x}. It's a tie, their is no winner! Let's Try Again")
elif (x == "rock") or (x == "ROCK") or (x == "Rock"):
    if c == "scissors":
        print("Rock smashes scissors! You are the winner!")
    else:
            print("Paper covers rock! Sorry you lost.")
elif (x == "paper") or (x == "PAPER") or (x == "Paper"):
    if c == "rock":
        print("Paper covers rock! You are the winner!")
    else:
        print("Scissors cuts paper! Sorry you lost.")
elif (x == "scissors") or (x == "SCISSORS") or (x == "Scissors"):
    if c == "paper":
        print("Scissors cuts paper! You are the winner!")
    else:
        print("Rock smashes scissors! Sorry you lost.")

print("Thank You For Participating In Our Game!!!")
again = x("Would you like to play another round?")

# print("Please Play Again Soon!")
exit()