# Write a program to find the sum of first n natural numbers using while loop.

num = int(input("Enter a natural number: "))

total = 0
i = 1
while i <= num:
    total += i
    i += 1

print(f"Sum of first {num} natural numbers is: {total}")
