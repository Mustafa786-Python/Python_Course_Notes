"""
1 for snake
-1 for water
0 for gun
"""
computer = 1
print("Snake: s, Gun: g, Water: w")
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reversedDict = {1: "Snake", -1: "Water", 0: "Gun" }
you = youDict[youstr]

print(f"You choose {reversedDict[you]} and computer choose {reversedDict[computer]}")

if computer == you:
    print("Its a draw")

else: 

    if computer == -1 and you == 1:
        print("You Win!")

    elif computer == -1 and you == 0:
        print("You Loose!")

    elif computer == 1 and you == 0:
        print("You Win!")

    elif computer == 1 and you == -1:
        print("You Loose!")

    elif computer == 0 and you == -1:
        print("You Win!")

    elif computer == 0 and you == 1:
        print("You Loose!")

