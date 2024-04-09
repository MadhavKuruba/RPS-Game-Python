# —----------------------------------
# Author: Madhav Kuruba  
# Program: RPS Game
# Version 
# Development Date(s): 7/10/2023
# —----------------------------------
import random
import pyfiglet
from rich import print

title = pyfiglet.figlet_format('RPS', font='isometric2')
print(f'[blue]{title}[/blue]___________________________________________')

replay = 1
while replay == 1:
    numGames = 0
    compWins = 0
    userWins = 0

    while numGames % 2 == 0:
        numGames = int(input("\n\nLet's Play 🪨, 📜, ✂️!\n\nEnter an (Odd) Number of Games: "))

    while compWins <= numGames // 2 and userWins <= numGames // 2:  

        userChoice = 0
        compChoice = 0

        while userChoice == compChoice:
            compChoice = random.randint(1, 3)
            userChoice = int(input("\nPick Your Move:\n\n1. Rock\n2. Paper\n3. Scissors\n\n"))

        if userChoice == 1:
            print("\nYour Choice: Rock 🪨")
        elif userChoice == 2:
            print("\nYour Choice: Paper 📜")
        elif userChoice == 3:
            print("\nYour Choice: Scissors ✂️")
        else:
            print("\nInvalid Input, Enter Number Corresponding to Option ❌")
            continue

        if compChoice == 1:
            print("Computer's Choice: Rock 🪨")
        elif compChoice == 2:
            print("Computer's Choice: Paper 📜")
        elif compChoice == 3:
            print("Computer's Choice: Scissors ✂️")

        if compChoice == userChoice:
            print("\nDraw")
        elif compChoice == 1 and userChoice == 2:
            print("\nYou Win! Great Job! 👍")
            userWins += 1
        elif compChoice == 1 and userChoice == 3:
            print("\nYou Lost. Better Luck Next Time. 😔")
            compWins += 1
        elif compChoice == 2 and userChoice == 1:
            print("\nYou Lost. Better Luck Next Time. 😔")
            compWins += 1
        elif compChoice == 2 and userChoice == 3:
            print("\nYou Win! Great Job! 👍")
            userWins += 1
        elif compChoice == 3 and userChoice == 1:
            print("\nYou Win! Great Job! 👍")
            userWins += 1
        elif compChoice == 3 and userChoice == 2:
            print("\nYou Lost. Better Luck Next Time. 😔")
            compWins += 1
        else:
            print("\nInvalid Input, Enter Number Corresponding to Option ❌")

        print("\nYou won {} time(s) and the Computer won {} time(s)".format(userWins, compWins))

    if userWins > numGames // 2:
        print("\nYou Won Against the Computer! Congratulations! 🏆")
    elif compWins > numGames // 2:
        print("\nThe Computer Won. Better Luck Next Time 🥈")
    else:
        print("Error")

    replay = int(input("\nWould You Like to Play Again?\n\n1. Yes\n2. No\n\n"))
