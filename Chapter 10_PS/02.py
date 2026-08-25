"""
Write a class “Calculator” capable of finding square, cube and square root of a
number
"""

class Calculator:
    def __init__(self, num):
        self.num = int(num)

    def square(self):
        square = self.num ** 2
        print(f"Sqaure of {self.num} = {square}")

    def cube(self):
        cube = self.num ** 3
        print(f"Cube of {self.num} = {cube}")

    def square_root(self):
        square_root = self.num ** 0.5
        print(f"Sqaure root of {self.num} = {square_root:.2f}")

#Taking option
while True:
    option = (input("Press: Sqaure = 1, Cube = 2, Square root = 3: ")).strip()
    if option in "1" or option in "2" or option in "3":
        break
    
    if not (option.isdigit()):
        print("Pres only 1, 2, 3", end="\n\n")


#Taking Input
while True:
    num = input("Enter the number: ")
    if num.isdigit():
        int(num)
        break
    else:
        print("Only Numbers",  end="\n\n")

#Creating Object
nums = Calculator(num)

option = int(option)
#Applying Conditions
if option == 1:
    nums.square()
elif option == 2:
    nums.cube()
else:
    nums.square_root()

