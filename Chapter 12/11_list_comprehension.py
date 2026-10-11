# num = [1, 2, 5, 10, 9]

# num_square = [i * i for i in num]

# print(num_square)

"Practice 2"

numbers = [1, 2, 3, 4, 5]
"""
squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)

"""
squares = [i**2 for i in numbers]
print(squares)

"Practice 3"

numbers = [3, 8, 11, 14, 17, 20, 25]

"""
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)
"""

even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)


"Practice 4"
words = ["python", "list", "comprehension", "coding"]
"""
uppercase_words = []

for word in words:
    uppercase_words.append(word.upper())

print(uppercase_words)

"""
uppercase_words = [word.upper() for word in words]
print(uppercase_words)

"Pracrtice 5"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
odd_squares = []

for number in numbers:
    if number % 2 != 0:
        odd_squares.append(number ** 2)

print(odd_squares)
"""
odd_squares = [number ** 2 for number in numbers if number % 2 != 0]
print(odd_squares)

"Practice 6"
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

"""
even_numbers = []

for row in matrix:
    for number in row:
        if number % 2 == 0:
            even_numbers.append(number)

print(even_numbers)
"""
even_numbers = [number for row in matrix for number in row if number % 2 == 0]
print(even_numbers)
