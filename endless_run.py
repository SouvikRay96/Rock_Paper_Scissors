import random

def infinite_rounds():
    user_score,computer_score = 0,0
    options = ["rock","paper","scissors","r","p","s"]
    print("Welcome to ENDLESS RUN")
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
        print("User input : {} , Computer pick : {}".format(user_input,computer_pick))
        print()
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
    
    #[print(key,':',value) for key, value in result.items()]
    return user_score,computer_score


