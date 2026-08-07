

numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "orange"}
set1 = {5, 10, 15, 20, 25}

a = set1 - numbers
b = set1.difference_update(numbers)
print(a)
print(b)
