"""
1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not
present, a message without exiting the program must be printed prompting the same.
"""

try: 
    with open("1.txt", "r") as file:
        read = file.read()
        print(f"\033[1mFile Data\033[0m")
        print(read, end= "\n\n")

except FileNotFoundError as e:
    print("The file \"1.txt\" does not exits")

#For file two:
try: 
    with open("2.txt", "r") as file:
        read = file.read()
        print(f"\033[1mFile Data\033[0m")
        print(read, end= "\n\n")

except FileNotFoundError as e:
    print("The file \"2.txt\" does not exits")

#For file three:
try: 
    with open("3.txt", "r") as file:
        read = file.read()
        print(f"\033[1mFile Data\033[0m")
        print(read, end= "\n\n")

except FileNotFoundError as e:
    print("The file \"3.txt\" does not exits")

