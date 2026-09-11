"""
1 for snake
-1 for water
0 for gun
"""
import random


computer = random.choice([1, -1, 0])
print("Snake: s, Gun: g, Water: w")
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reversedDict = {1: "Snake", -1: "Water", 0: "Gun"}
you = youDict[youstr]

print(
    f"You choose {reversedDict[you]} and computer choose {reversedDict[computer]}")

if computer == you:
    print("Its a draw")

else:
    """
        if computer == -1 and you == 1:
            print("You Win!") 

        elif computer == -1 and you == 0:
            print("You Loose!") = -1

        elif computer == 1 and you == 0:
            print("You Win!")

        elif computer == 1 and you == -1:
            print("You Loose!") = 2

        elif computer == 0 and you == -1:
            print("You Win!")

        elif computer == 0 and you == 1:
            print("You Loose!") -1
    """

    if (computer - you) == -1 or (computer - you) == 2:
        print("You Loose")

    else:
        print("You Win")
