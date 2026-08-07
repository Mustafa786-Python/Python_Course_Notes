'''
Write a program which finds out whether a given name is present in a list or not.
'''
names = ["Ali", "Hussain", "Fatima", "Danish", "Zain", "Ahmed", "Sara", "Hina", "Raza", "Ayesha"] #creating list of then names
print(names)
enter = input("Enter a name: ").strip().title() #taking input from user
#Applying if and else condition
if enter in names:
    print(f"Yes {enter} is present in our list ")
else:
    print(f"No, {enter} is not present in our list ")

