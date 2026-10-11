"""
5. Write a program to find the maximum of the numbers in a list using the reduce
function.
"""
from functools import reduce
from random import sample

numbers = sample(range(100, 1000 + 1), 10)
print(numbers)


def greater(x, y): return x if x > y else y


maximum = reduce(greater, numbers)
print(maximum)
