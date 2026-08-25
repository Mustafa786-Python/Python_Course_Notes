"""
4. A file contains a word “Donkey” multiple times. You need to write a program
which replace this word with ##### by updating the same file.
"""
word = "Donkey"

with open("donkey.txt", "r") as f:
    content = f.read()

new_content = content.replace(word, "####")


with open("donkey.txt", "w") as f:
    f.write(new_content)
