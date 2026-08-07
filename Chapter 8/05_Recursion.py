def factorail(n):
    if (n == 1 or n == 0):
        return 1
    return n * factorail(n -1)

n = int(input("Enter a number: "))
print(f"The factorial of the {n} is {factorail(n)}")
