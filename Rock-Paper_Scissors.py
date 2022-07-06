"""ROCK-PAPER-SCISSORS"""

# Importing random module so as to generate random computer pick 
import random
# Declaring two variables user_score and computer_score
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
    print()
    print("Type ROCK/PAPER/SCISSORS/r/p/s/R/P/S or QUIT/Q/q ... ")
    user_input = input("Enter : ").lower() # Taking the user input
    if user_input == "q":
        print("Exiting from the Game !!! GOODBYE !!!")
        print()
        # If the user wants to quit the game
        break
    if user_input not in options:
        print("Please enter correctly...")
        print()
        # If the user enters an invalid option
        continue

    random_number = random.randint(0,2) # Generating the random computer pick
    # rock --> 0 ; paper --> 1 ; scissors --> 2
    computer_pick = options[random_number]
    # If the user enters rock and the computer picks scissors , then the user wins
    if (user_input == "r" or user_input == "rock") and computer_pick == "scissors":
        print("You WIN !!!")
        user_score += 1
    # If the user enters paper and the computer picks rock , then the user wins
    elif (user_input == "p" or user_input == "paper") and computer_pick == "rock":
        print("You WIN !!!")
        user_score += 1
    # If the user enters scissors and the computer picks paper , then the user wins
    elif (user_input == "s" or user_input == "scissors") and computer_pick == "paper":
        print("You WIN !!!")
        user_score += 1
    # if the above conditions are not satisfied then computer wins
    else:
        print("Computer WIN !!!")
        computer_score += 1
# Printing the final results i.e. who won the game
print("--------------------------------------------------------------------------")
print("THE FINAL RESULTS ... ")
score = {"User Score" : user_score, "Computer Score" : computer_score}
# Displaying the user score and computer score
[print(key,':',value) for key, value in score.items()]
# If the user score is more than the computer score then the user wins
if user_score > computer_score :
    print("Hurray!!! You win the game")
# If the user score and the computer score is equal then the game is draw
elif user_score == computer_score :
    print("It's a DRAW")
# If the computer score is more than the user score then the user looses the game
else:
    print("Sorry!!! You lost")
print("Hope you Enjoyed")
print("--------------------------------------------------------------------------")


