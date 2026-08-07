"""
You receive student marks.

Remove the most recently entered student

Show which student was removed

Show remaining students
"""


students = {
    "Ali": 85,
    "Sara": 92,
    "Ahmed": 78,
    "Fatima": 88,
    "Hassan": 90
}

"Task1"
print(f"The before update dict {students}")
return1 = students.popitem()
print(f"The removed item {return1}")
print(f"The updated dict {students}")
