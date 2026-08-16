"""1. Write a program to read the text from a given file ‘poems.txt’ and find out
whether it contains the word ‘twinkle’.
"""

with open("poem.txt", "r") as f:
    data = f.read()
    if "Twinkle" in data:
        print("Yes it is")
    else:
        print("No it is not")
