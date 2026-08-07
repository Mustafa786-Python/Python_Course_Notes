"""
Write a python program to display a user entered name followed
by Good Afternoon using input () function.
"""
name = input("Enetr your first name: ")
name2 = input("Enter your last name: ")
print(f"Good Afternoon \033[1m{name.title()} {name2.title()}\033[0m")
