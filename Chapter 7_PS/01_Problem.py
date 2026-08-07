# Write a program to print multiplication table of a given number using for loop
intro = f"""
Welcome to the table calculater. It will create a table based on the number given\n
"""
print(intro)

while True:
    num = int(input("Enter a number for table: "))  # Taking input form the user
    for i in range(1, 10 + 1):
       table = i * num
       print(f"{i} x {num} = {table}")
    info = input("Do you want to continue: ").lower().strip()
    if "no" in info:
        break
