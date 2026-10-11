"""
4. Write a program to filter a list of numbers which are divisible by 5.
"""

import random

numbers = random.sample(range(50, 501), 10)
print(numbers)


def div_by_5(x): return x % 5 == 0


numbers_div_5 = list(filter(div_by_5, numbers))
print(numbers_div_5)
