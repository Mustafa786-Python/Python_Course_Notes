# Write a recursive function to calculate the sum of first n natural numbers.
def sum1(n):
    if n <= 0:
        text = "Invalid Input!"
        return text
    if n == 1:
        return 1
    return n + sum1(n - 1)

#for taking multiple times
n = int(input("Enter a natrul number for sum: "))
print(sum1(n))
n = int(input("Enter a natrul number for sum: "))
print(sum1(n))
n = int(input("Enter a natrul number for sum: "))
print(sum1(n))
