import random

print("--This is the game of guesses!\n--You must guess the numbers that I'm holding\n")
playerName = input("--What is your name?\n")
print("\n--Welcome {}".format(playerName))
gamePlay = "y"


while gamePlay == "y":

    # win = 1 represents you have won the game. 0 represents that you have lost.
    win = 0
    selection = int(input(
        "--You'd like to guess the number between... (type 1 or 2)\n1. 1-10\n2. 1-100\n"))

    if selection == 1:  # 1-10
        random_number = random.randint(1, 10)
        chance = 3
        print("\n--Ha ha are you afraid? Then start guessing. You have {} chances.\n--But don't worry, I'll help you as much as I can.\n".format(chance))

    elif selection == 2:  # 1-100
        random_number = random.randint(1, 100)
        chance = 5
        print("\n--This is a bit of harder than the other one. You have {} chances. Good luck!\n".format(chance))

    while (chance != 0):
        answer = int(input("Your guess is: "))
        if answer == random_number:
            print("\nGood job. You got the answer.")
            win = 1
            break
        else:
            chance = chance - 1
            if chance == 0:
                print(
                    "--Oops, that was wrong. You have no chances left. The answer was {}\n".format(random_number))
            elif answer > random_number:
                print(
                    "\n--Oops, that was wrong. You should go lower. You have left {} chances".format(chance))
            else:
                print(
                    "\n--Oops, that was wrong. You should go higher. You have left {} chances".format(chance))

    if win == 1:
        gamePlay = input("\n--Would you like to play again (y/n): ")
        gamePlay.lower()
    else:
        gamePlay = input(
            "--Don't worry. You'll win next time. Would you like to play again (y/n): ")
        gamePlay.lower()
