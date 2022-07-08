import rules_of_game
import endless_run
import round_of_mode1
import final_results



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
        user_score,computer_score = round_of_mode1.round_of(number)
        # Calling the function round_of by passing the point barrier as the parameter
    elif ch == 2:
        user_score,computer_score = endless_run.infinite_rounds()
        # Calling the function infinite_rounds
    elif ch == 3:
        rules_of_game.rules() # To display the rules of the game
    elif ch == 4:
        final_results.display_results(user_score,computer_score) # Calling the display function to display the results
    elif ch == 5:
        # exiting the game
        print("GOODBYE !!! HOPE YOU ENJOYED THE GAME... PLEASE VISIT NEXT TIME... THANK YOU")
        print()
        break
    else:
        print()
        print("Invalid choice !!! PLEASE ENTER AGAIN")
        print()

    
    



