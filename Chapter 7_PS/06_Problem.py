# Write a program to calculate the factorial of a given number using for loop.
'FInding Factorial'
num = int(input("Enter a number: "))
fact = 1
# if num == 0:
#     print(f"The factorial of 0 is {fact}")
# else:
#     for i in range(num, 1, -1):
#         fact *= i
# print(f"The factorial of {num} is {fact}")

"Harry Version"
for i in range(1, num+1):
    fact *= i
print(f"The factorial of Harry's Version {num} is {fact}")