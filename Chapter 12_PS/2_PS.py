"""
2. Write a program to print third, fifth and seventh element from a list using enumerate
function.
"""
numbers = [1, 5, 10, 15, 20, 25, 30, 39]

for i, num in enumerate(numbers):
    if i == 2 or i == 4 or i == 6: 
        print(num)
