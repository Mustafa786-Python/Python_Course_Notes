from random import randint

n = randint(1, 100)
a = -1
guess = 1

while (a != n):
    a = int(input("Enter yout guess number: "))

    if a > n:
        print("High Guess", end="\n\n")
        guess += 1

    elif a < n:
        print("Lower Guess", end="\n\n")
        guess += 1

print(f"You guessed the number in {guess} attempts")
