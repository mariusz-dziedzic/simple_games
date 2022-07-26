# Rock, Paper, Scissors
import random
import time
repeat = "Y"
name = input("Enter your name: ")
if not name:
    name = 'User'
time.sleep(0.3)
print(f"Welcome {name}!")
confirmation = ['y', 'yy', 'yyy', 'Y', 'yes', 'Yes', 'YES', 'T', 't', 'u', 'U']
accept = input("Do you want to start the game? [Y/N]: ")
time.sleep(0.3)
if accept in confirmation:
    print("Okay, let's play.")
    time.sleep(0.3)
    print("_"*42)
    print()
    time.sleep(0.3)
    print("We start the game of Paper, Rock, Scissors!")
    while repeat in confirmation:
        time.sleep(0.3)
        try:
            round = int(input("How many points do you want to play to? "))
        except:
            print('You must have entered something wrong. Then we will play to 3 points')
            round = 3
        if round < 1:
            print("Very funny")
            break

        time.sleep(0.3)
        print("Now enter the number 1-3:")
        print("1 - Paper")
        print("2 - Rock")
        print("3 - Scissors")

        point_my = 0
        point_pc = 0
        options = [1, 2, 3]
        game = 1
        while point_my <= round-1 and point_pc <= round-1:
            print("_"*42)
            print()
            print(f"ROUND {game} ---------- {name} ({point_my}:{point_pc}) AI")
            x = input("Enter the number 1-3: ")
            time.sleep(0.3)
            pc = (random.choice(options))
            if x == "1":
                print("You chose Paper.")
            elif x == "2":
                print("You chose Rock.")
            elif x == "3":
                print("You chose Scissors.")
            elif x == "":
                print("Boom?")
            else:
                x = ''
                print("Boom?")
                # point_pc += 1
            time.sleep(0.3)
            if pc == 1:
                print("AI chose Paper.")
            elif pc == 2:
                print("AI chose Rock.")
            elif pc == 3:
                print("AI chose Scissors.")
            else:
                print("Boom?")
            time.sleep(0.3)
            if x == "":
                print("Something is wrong, so point for AI.")
                point_pc += 1
            elif int(x) == pc:
                print("We have got a draw!")
            elif x == "1" and pc == 2:
                print("You won the round!")
                point_my += 1
            elif x == "1" and pc == 3:
                print("You lost a round!")
                point_pc += 1
            elif x == "2" and pc == 1:
                print("You lost a round!")
                point_pc += 1
            elif x == "2" and pc == 3:
                print("You won the round!")
                point_my += 1
            elif x == "3" and pc == 1:
                print("You won the round!")
                point_my += 1
            elif x == "3" and pc == 2:
                print("You lost a round!")
                point_pc += 1
            else:
                print("Something is wrong, so point for AI.")
            game += 1

        print("_"*42)
        print()
        time.sleep(0.7)
        print("END. Here are the results: ")
        time.sleep(0.3)
        print(f"You got: {point_my} p.")
        time.sleep(0.3)
        print(f"AI got: {point_pc} p.")
        time.sleep(0.3)

        if point_my > point_pc and point_pc == 0:
            print("Beautiful victory! To zero.")
        elif point_my > point_pc:
            print("Beautiful Victory!")
        elif point_my < point_pc:
            print("Unfortunately a defeat.")
        else:
            print("Error?")
        print("_"*42)

        repeat = input("Do you want to play again? [Y/N]: ")
        print()
    else:
        print("Thank you for the game ;)")
elif accept == "n" or accept == "N":
    print("Only cowards run away without a fight!")
else:
    print("Invalid command. Start over")

input()
