"""ROCK-PAPER-SCISSORS"""


import random

user_score,computer_score = 0,0
options = ["rock","paper","scissors","r","p","s"]
print("--------------------------------------------------------------------------")
print("Game of ROCK-PAPER-SCISSORS")
print("--------------------------------------------------------------------------")
print("1) Rock --> Type R/r/rock")
print("2) Paper --> Type P/p/paper")
print("3) Scissors --> Type S/s/scissors")
print("4) Quit --> Type Q/q")
print("--------------------------------------------------------------------------")

while True:
    print("Type ROCK/PAPER/SCISSORS/r/p/s/R/P/S or QUIT/Q/q ... ")
    user_input = input("Enter : ").lower()
    if user_input == "q":
        print("Exiting from the Game !!! GOODBYE !!!")
        break
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock --> 0 ; paper --> 1 ; scissors --> 2
    computer_pick = options[random_number]
    if (user_input == "r" or user_input == "rock") and computer_pick == "scissors":
        print("You WIN !!!")
        user_score += 1
    elif (user_input == "p" or user_input == "paper") and computer_pick == "rock":
        print("You WIN !!!")
        user_score += 1
    elif (user_input == "s" or user_input == "scissors") and computer_pick == "paper":
        print("You WIN !!!")
        user_score += 1
    else:
        print("Computer WIN !!!")
        computer_score += 1

print("--------------------------------------------------------------------------")
print("THE FINAL RESULTS ... ")
score = {"User Score" : user_score, "Computer Score" : computer_score}
[print(key,':',value) for key, value in score.items()]
if user_score > computer_score :
    print("Hurray!!! You win the game")
elif user_score == computer_score :
    print("It's a DRAW")
else:
    print("Sorry!!! You lost")
print("Hope you Enjoyed")
print("--------------------------------------------------------------------------")


