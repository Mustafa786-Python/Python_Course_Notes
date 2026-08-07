# Attempt problem 1 using while loop
while True:
    # Taking input form the user
    num = int(input("Enter a number for table: "))
    i = 1
    while i < 10 + 1:
        table = i * num
        print(f"{i} x {num} = {table}")
        i += 1
    info = input("Do you want to continue: ").lower().strip()
    if "no" in info:
        break
