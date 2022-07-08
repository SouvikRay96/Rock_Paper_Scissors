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