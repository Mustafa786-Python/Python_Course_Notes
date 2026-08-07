"""
Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*
"""


def star(num):
    for i in range(0, num+1):
        if i == 0:
            star = "*" * num
            print(star)
        else:
            star = "*" * (num - i)
            print(star)


star(3)

# Harry's Version
# By using recursion


def pattern(n):
    if n == 0:
        return
    print("*" * n)
    pattern(n - 1)


pattern(3)
