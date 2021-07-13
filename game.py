# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

# ASK FOR A USER INPUT
# source: python.org
# = input('--> ')

x = input("Please, choose one of the following: rock, paper, or scissors: ")
# print(x)

# VALIDATE THE USER INPUT

# if x == "rock": # "paper" "scissors"
# print("VALID")
# else:
# print("OOPS, INVALID, PLEASE TRY AGAIN")
# exit()


if (x == "rock") or (x == "paper") or (x == "scissors") or (x == "ROCK") or (x == "Rock") or (x == "Paper") or (x == "PAPER") or (x == "Scissors") or (x == "SCISSORS"):
    print(f"{x} is a Valid Entry!")
     # using the f before string - Source: https://www.kite.com/python/answers/how-to-print-a-variable-with-a-string-in-python
else:
    print(f"Sorry, {x} is an Invalid Entry.")
     # using the f before string - Source: https://www.kite.com/python/answers/how-to-print-a-variable-with-a-string-in-python
    print("Please, only select one of the following: rock, paper, or scissors.")
    exit()

# print("LATER MESSAGES")

# print("Game Summary:")

print('\033[1mGAME SUMMARY: \033[0m')
# Source: Bold print: https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python/8930747
# Source: 1 line of bold text: https://stackabuse.com/how-to-print-colored-text-in-python

print("USER CHOICE:", x)

# GENERATE A COMPUTER CHOICE

valid_options = ["rock", "paper", "scissors"] # this is a list

c = random.choice(valid_options)

print("COMPUTER CHOICE:", c)
# print(random.choice(valid_options))

print('\033[1mResults: \033[0m')
# Source: Bold print: https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python/8930747
# Source: 1 line of bold text: https://stackabuse.com/how-to-print-colored-text-in-python

# Determing Winner
# Source: https://realpython.com/python-rock-paper-scissors/

if x == c:
    print(f"Both players have selected {x}. It's a tie and there is no winner! Please Try Again.")
    # using the f before message - Source: https://www.kite.com/python/answers/how-to-print-a-variable-with-a-string-in-python
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

print("Thank You For Participating!!!")
print("Please, Play Again Soon!")
exit()
