# Write a program to print multiplication table of n using for loops in reversed order

while True:
    num = int(input("Enter a number: "))
    for i in range(10, 0, -1):
        table = num * i
        print(f"{num} x {i} = {table}")
    option = input("Do you want to continue (Yes/No): ").lower().strip()
    if "no" in option:
        break

"Harry's Version"
while True:
    for b in range(1, 10 + 1):
        print(f"{num} X {11 - b} = {num*(11 - b)}")
    option = input("Do you want to continue (Yes/No): ").lower().strip()
    if "no" in option:
        break
