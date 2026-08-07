""" Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user. """
num1 = int(input("Enter marks of first subject: "))
num2 = int(input("Enter marks of second subject: "))
num3 = int(input("Enter marks of third subject "))

total_marks = num1 + num2 + num3
percentage = total_marks/3

"My way for finding"
# #Subject wise 
# if num1 <= 33:
#     print(f"\nYou are fail in first subject") #for num 1
# else: 
#    print(f"\nYou are passed in first subject")

# if num2 <= 33:
#   print(f"\nYou are fail in second subject") #for num 2
# else:
#     print(f"\nYou are passed in second subject")

# if num3 <= 33:
#     print(f"\nYou are fail in third subject") #for num 3
# else: 
#   print(f"\nYou are passed in third subject")

# #total percentage
# if percentage <= 40:
#     print(f"\nYou are faild. You get {percentage}% in the test")
# else:
#     print(f"Congratulations! You are not failed. You get {percentage}% in the test")

"Harry's Way for finding"
if (percentage >= 40 and num1 >= 33 and num2 >= 33 and  num3 >= 33):
    print(f"You are Passed.\tYour percentage is {percentage}")
else:
    print(f"You are Fail.\tYour percentage is {percentage}")

