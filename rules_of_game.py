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
            print("Round of Mode : ")
            print("In this gaming mode the user gives a point barrier such as 'n'")
            print("And whosoever reaches the point barrier first wins the game.")
            print("Suppose the user gave 5 as a point barrier...")
            print("If the user scores 5 points first then the user wins the game...")
            print("And if the computer scores 5 points first then the computer wins the game.")
            print("--------------------------------------------------------------------------")
        elif ch == 2:
            print("--------------------------------------------------------------------------")
            print("Endless Run : ")
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