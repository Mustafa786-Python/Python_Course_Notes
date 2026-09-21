a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if (b == 0):
    raise ZeroDivisionError("Nothing can be divided by 0")
print(round((a / b), 2))