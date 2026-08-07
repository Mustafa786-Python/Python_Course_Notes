# Write a program to store seven fruits in a list entered by a user.
fruit_1 = input("Enter fruit 1: ")
fruit_2 = input("Enter fruit 2: ")
fruit_3 = input("Enter fruit 3: ")
fruit_4 = input("Enter fruit 4: ")
fruit_5 = input("Enter fruit 5: ") 
fruit_6 = input("Enter fruit 6: ")
fruit_7 = input("Enter fruit 7: ")
fruit_list = [fruit_1, fruit_2, fruit_3, fruit_4, fruit_5, fruit_6, fruit_7]
print(fruit_list)

"Making this function by using loop"
fruit_list_2 = []
for i in range(1, 7 + 1):
    f = input(f"Enter fruit {i} : ")
    fruit_list_2.append(f)
print(fruit_list_2)

# left delete press backspace
# Right delete press delete key