"""Create an empty dictionary. Allow 4 friends to enter their favorite language as 
value and use key as their names. Assume that the names are unique."""
data = {}
for i in range(4):
    lan = input("Enter a language name: ").strip().title()
    name = input("Enter your name: ").strip().title()
    data[lan] = name
print(data, type(data))
data.clear()
print(data)