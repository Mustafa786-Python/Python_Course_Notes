"""
Write a program to print the following star pattern.
* * *
*   * for n = 3
* * *
# """
n = int(input("Enter a number: "))

# "Creation with the help of chat gpt"
# if n <= 0:
#     print("n must be positive")
# elif n == 1:
#     print("*")
# else:
#     for i in range(n):
#         if i == 0 or i == n - 1:
#             print("* " * n)
#         else:
#             # First star, inner spaces, last star
#             print("* " + "  " * (n - 2) + "*")

"Harry version"
for i in range(1, n+1):
    if (i == 1 or n == i):
        print('*'*n, end="")
    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*", end="")
    print("")
