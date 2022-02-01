import random
import rps

print("Hello, I am a ghost.\nLet's play Rock, Paper, Scissors!\nType a corresponding letter to make your choice.")
player_choice = input("\nR = Rock\nP = Paper\nS = Scissors\n\nYour choice is: ")

if player_choice == "R":
    print(rps.rock)
    print("\n You chose ROCK!")
elif player_choice == "P":
    print(rps.paper)
    print("\nYou Chose PAPER!")
elif player_choice == "S":
    print(rps.scissors)
    print("\nYou Chose SCISSORS!")

ghost = ["R", "P", "S"]
random_ghost = random.randint(0, 2)

#DRAW situations
if player_choice == "R" and ghost[random_ghost] == "R":
    print(rps.rock)
    print("\nThe ghost also chose ROCK as well.\nThe game is a DRAW!")
elif player_choice == "P" and ghost[random_ghost] == "P":
    print(rps.paper)
    print("\nThe ghost also chose PAPER as well.\nThe game is a DRAW!")
elif player_choice == "S" and ghost[random_ghost] == "S":
    print(rps.scissors)
    print("\nThe ghost also chose SCISSORS as well.\nThe game is a DRAW!")

#Player WIN situations
elif player_choice == "R" and ghost[random_ghost] == "S":
    print(rps.scissors)
    print("\nThe ghost chose SCISSORS.\nYOU WIN!")
elif player_choice == "P" and ghost[random_ghost] == "R":
    print(rps.rock)
    print("\nThe ghost chose ROCK.\nYOU WIN!")
elif player_choice == "S" and ghost[random_ghost] == "P":
    print(rps.paper)
    print("\nThe ghost chose PAPER.\nYOU WIN!")

#Player LOSE situations
elif player_choice == "R" and ghost[random_ghost] == "P":
    print(rps.paper)
    print("\nThe ghost chose PAPER.\nYOU LOSE!")
elif player_choice == "P" and ghost[random_ghost] == "S":
    print(rps.scissors)
    print("\nThe ghost chose SCISSORS.\nYOU LOSE!")
elif player_choice == "S" and ghost[random_ghost] == "R":
    print(rps.rock)
    print("\nThe ghost chose ROCK.\nYOU LOSE!")
