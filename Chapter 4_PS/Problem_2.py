#Write a program to accept marks of 6 students and display them in sorted manner.
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
number3 = int(input("Enter number 3: "))
number4 = int(input("Enter number 4: "))
number5 = int(input("Enter number 5: "))
number6 = int(input("Enter number 6: "))
number7 = int(input("Enter number 7: "))

number_list = [number1, number2, number3, number4, number5, number6, number7] 
print(sorted(number_list))