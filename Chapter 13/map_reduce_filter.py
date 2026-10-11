from functools import reduce

# map: It helps to format all values.

l = [1, 3, 5, 7, 8]


def square(x): return x**2


sqlist = map(square, l)
print(list(sqlist))

# Filter Example:

numbers = list(range(1, 11))


# def even(n):
#     if (n % 2 == 0):
#         return True
#     return False

def even(n): return n % 2 == 0


even_num = filter(even, numbers)
print(list(even_num))


# Reduce Example
def add(x, y): return x + y

print("Total sum of numbers")
total = reduce(add, numbers)
print(total, end="\n\n")


