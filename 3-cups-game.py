# 3 Cups Game
import random
import time
print("-"*48)
print("Welcome to Casino De Dzicz! \nMake yourself at home.\n")
time.sleep(0.3)
print("We start the game with 3 cups!\nThe rules are simple:")
print("- You point to a cup that may contain a ball.")
print("- If you guess you get double your bet.")
print("- However, when you miss, you lose your stake.")
print("- You can also play for 0 stakes to practice the rules.\n")
time.sleep(0.3)
try:
    balance = int(input("Enter the amount you want to pay: "))
    if balance < 0:
        balance = 0
    print("Your budget is now:", balance)
except:
    print("Something is wrong. We'll give you $ 1 to start")
    balance = 1

confirmation = ['y', 'yy', 'yyy', 'Y', 'yes', 'Yes', 'YES', 'T', 't', 'u', 'U']
game = "Y"
repeat = "Y"
while game in confirmation:

    if balance <= 0 and repeat == "Y":
        time.sleep(0.3)
        print("-"*48)
        print("You are poor")
        payment = str(input("Do you want to make a deposit? [Y/N]: "))
        if payment in confirmation:
            balance = int(input("Enter the amount you want to pay: "))
            if balance < 0:
                balance = 0
        else:
            repeat = "N"
            print("Okay, then you come out with nothing")

    elif balance > 0:
        time.sleep(0.3)
        print("-"*48)

        options = [1, 2, 3]
        try:
            stake = int(input("Enter the stake you want to play: "))
            if stake < 0:
                print("Okay prankster, so you're playing for 0")
                stake = 0
        except:
            print("Something is wrong. Let's play for 0 this time")
            stake = 0
        if stake > balance:
            print("You don't have that much ")
            print("You can play for a maximum of", balance)

        else:
            balance -= stake
            print("Mixing the cups...")
            time.sleep(1)
            print("   _____   "*3)
            print("**/     \**"*3)
            print("**|     |**"*3)
            print("**|  1  |****|  2  |****|  3  |**")
            print("**|     |**"*3)
            print("***********"*3)
            print()

            try:
                type = int(input("Choose a cup 1-3: "))
            except:
                print("Let's be serious")
            if type not in options:
                type = (random.choice(options))
                print("Okay, we'll draw a cup for you:", type)
            pc = (random.choice(options))
            time.sleep(0.3)
            print("The ball was in the cup number:", pc)
            time.sleep(0.3)

            if type == pc:
                balance += stake*2
                print("Well done! Now in your account you have:", balance)
            else:
                print("Unfortunately. You now have in your account:", balance)
            print("-"*48)
            time.sleep(0.3)
            game = input("Do you want to play again? [Y/N]: ")
    else:
        game = "N"

if game not in confirmation:
    time.sleep(0.3)
    print("Thanks for the game")
    print("You leave with the amount:", balance)
input()
