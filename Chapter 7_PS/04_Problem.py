# Write a program to find whether a given number is prime or not.
# Taking input form the user
num = int(input("Enter the a number: "))
# Making condition for primenumers:
"AI Version"
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} The number is less than 1.")

"Harry Version"
for i in range(2, num):
    if (num % i) == 0:
        print(f"{num} is not prime")
        break
else:
    print(f"{num} is prime")
"""
Explanation:
in this the "for loop" will run it finds a divisor. if not the "loop" will end.
The "else" is not part of the "if" instead it is the part of "for loop"
"""
