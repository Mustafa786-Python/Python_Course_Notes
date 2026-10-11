"""
3. A list contains the multiplication table of 7. write a program to convert it to vertical
string of same numbers.
"""

table_of_7 = [7 * i for i in range(1, 11)]
vertical_in_string = "\n".join(map(str, table_of_7))
print(vertical_in_string)
