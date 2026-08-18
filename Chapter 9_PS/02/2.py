
def game():
    score = input("Enter Score: ")

    with open("Hi-Score.txt", "w") as f:
        f.write(score)


game()
