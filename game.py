# game.py

print("Rock, Paper, Scissors, Shoot!")

# ASK FOR A USER INPUT
# source: python.org
#s = input(--->)

x = input("Please choose one of 'rock', 'paper', scissors'")
print(x)

# VALIDATE THE USER INPUT

# if x == "rock": # "paper" "scissors"
#     print("VALID")
# else:
#     print("OOPS, INVALID, PLEASE TRY AGAIN")
#     exit()


if (x == "rock") or (x == "paper") or (x == "scissors"):
    print("VALID")
else:
    print("OOPS, INVALID, PLEASE TRY AGAIN")
    exit()

print("LATER MESSAGES")



# GENERATE A COMPUTER CHOICE


# DETERMINE A WINNER



