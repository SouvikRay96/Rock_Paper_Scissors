"""ROCK-PAPER-SCISSORS"""

# Importing random module so as to generate random computer pick 
import random


def rules():
    print("--------------------------------------------------------------------------")
    print("The rules of the Game and the Game modes ... ")
    while True:
        print("1) Round Of Mode ...")
        print("2) Infinte rounds / Endless run...")
        print("3) User input Criteria ... ")
        print("4) Exit the rules --> Return to main menu...")
        ch = int(input("Which rule details you want to see : "))
        if ch == 1:
            print("--------------------------------------------------------------------------")
            print("In this gaming mode the user gives a point barrier such as 'n'")
            print("And whosoever reaches the point barrier first wins the game.")
            print("Suppose the user gave 5 as a point barrier...")
            print("If the user scores 5 points first then the user wins the game...")
            print("And if the computer scores 5 points first then the computer wins the game.")
            print("--------------------------------------------------------------------------")
        elif ch == 2:
            print("--------------------------------------------------------------------------")
            print("In this gaming mode the user and the computer plays for endless/infinite number of points")
            print("And whosoever scores the maximum wins the game...")
            print("This run will continue until the user wants to quit...")
            print("--------------------------------------------------------------------------")
        elif ch == 3:
            print("--------------------------------------------------------------------------")
            print("Game of ROCK-PAPER-SCISSORS user input Citeria")
            print("--------------------------------------------------------------------------")
            print("1) Rock --> Type R/r/rock")
            print("2) Paper --> Type P/p/paper")
            print("3) Scissors --> Type S/s/scissors")
            print("4) Quit --> Type Q/q")
            print("--------------------------------------------------------------------------")
        elif ch == 4:
            print("--------------------------------------------------------------------------")
            print("Hope you will enjoy the game...")
            print("THANK YOU")
            print("--------------------------------------------------------------------------")
            break
        else:
            print()
            print("Wrong choice ... Enter Again !!!")
            print()


def display_results(user_score,computer_score):
    print("--------------------------------------------------------------------------")
    print("THE FINAL RESULTS ... ")
    print()
    # Displaying the user score and computer score
    #[print(key,':',value) for key, value in result.items()
    print("User Score : {} \nComputer Score : {}".format(user_score,computer_score))
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



def round_of(number):
    user_score,computer_score = 0,0
    options = ["rock","paper","scissors","r","p","s"]
    while True:
        print()
        print("Type ROCK/PAPER/SCISSORS/r/p/s/R/P/S ... ")
        user_input = input("Enter : ").lower() # Taking the user input
        
        if user_input not in options:
            print("Please enter correctly...")
            print()
            # If the user enters an invalid option
            continue

        random_number = random.randint(0,2) # Generating the random computer pick
        # rock --> 0 ; paper --> 1 ; scissors --> 2
        computer_pick = options[random_number]
        print()
        print("User input : {} , Computer pick : {} \n".format(user_input,computer_pick))
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
        # if both the user input and the computer random are rock then no scores will be added to both
        elif (user_input == "r" or user_input == "rock") and computer_pick == "rock":
            print("Since both are same ... No score added to both")
        # if both the user input and the computer random are paper then no scores will be added to both
        elif (user_input == "p" or user_input == "paper") and computer_pick == "paper":
            print("Since both are same ... No score added to both")
        # if both the user input and the computer random are scissors then no scores will be added to both
        elif (user_input == "s" or user_input == "scissors") and computer_pick == "scissors":
            print("Since both are same ... No score added to both")
        # if the above conditions are not satisfied then computer wins
        else:
            print("Computer WIN !!!")
            computer_score += 1
        if user_score == number or computer_score == number:
            break
    #result = {"User Score" : user_score, "Computer Score" : computer_score}
    return user_score,computer_score


def infinite_rounds():
    user_score,computer_score = 0,0
    options = ["rock","paper","scissors","r","p","s"]
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
        print() # Displaying the user input and computer random pick
        print("User input : {} , Computer pick : {} \n".format(user_input,computer_pick))
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
        # if both the user input and the computer random are rock then no scores will be added to both
        elif (user_input == "r" or user_input == "rock") and computer_pick == "rock":
            print("Since both are same ... No score added to both")
        # if both the user input and the computer random are paper then no scores will be added to both
        elif (user_input == "p" or user_input == "paper") and computer_pick == "paper":
            print("Since both are same ... No score added to both")
        # if both the user input and the computer random are scissors then no scores will be added to both
        elif (user_input == "s" or user_input == "scissors") and computer_pick == "scissors":
            print("Since both are same ... No score added to both")
        # if the above conditions are not satisfied then computer wins
        else:
            print("Computer WIN !!!")
            computer_score += 1
    #result = {"User Score" : user_score, "Computer Score" : computer_score}
    #[print(key,':',value) for key, value in result.items()]
    return user_score,computer_score

user_score,computer_score = 0,0
while True:
    print()
    print("------------------------------------------------------------------------")
    print("Welcome to the game of ROCK_PAPER_SCISSORS ")
    print("------------------------------------------------------------------------")
    print("The game modes : ")
    print("1) Round of mode")
    print("2) Infinite Run ")
    print("3) View the rules of the game ")
    print("4) View the results ")
    print("5) Exit the game")
    print("Select the mode in which ypu want to play ... ")
    ch = int(input("TYPE YOUR OPTION: "))
    print("------------------------------------------------------------------------")
    print()
    if ch == 1:
        number = int(input("What is the point barrier you want to compete with : "))
        user_score,computer_score = round_of(number)
        # Calling the function round_of by passing the point barrier as the parameter
    elif ch == 2:
        user_score,computer_score = infinite_rounds()
        # Calling the function infinite_rounds
    elif ch == 3:
        rules() # To display the rules of the game
    elif ch == 4:
        display_results(user_score,computer_score) # Calling the display function to display the results
    elif ch == 5:
        # exiting the game
        print("GOODBYE !!! HOPE YOU ENJOYED THE GAME... PLEASE VISIT NEXT TIME... THANK YOU")
        break
    else:
        print()
        print("Invalid choice !!! PLEASE ENTER AGAIN")
        print()



