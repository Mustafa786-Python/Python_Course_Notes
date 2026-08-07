"""
Write a program to print the following star pattern.
 *
***
***** for n = 3
"""
print(f"""
                                   Welcome to Star generator
""")
num = int(input("Enter a number: "))
print(f"\n")
for i in range(1, num + 1):
    print(" " * (num-i), end="")
    print("*" * (2*i-1), end="")
    print("")
print(f"\n")
