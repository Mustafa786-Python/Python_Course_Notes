'''
Write a program to calculate the grade of a student from his marks from the 
following scheme:
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 =>C
50 – 60 => D
<50 => F
'''
print(f"""
Welcome to the tool that will percentage calculater of 7 federal board subjects
      See our grading sort:
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 =>C
50 – 60 => D
<50 => F
""")
# Taking input form user
total_marks = int(input("Enter the total marks :"))

mark1 = int(input("Enter the marks of Maths/Biology :"))
mark2 = int(input("Enter the marks of English :"))
mark3 = int(input("Enter the marks of Urdu :"))
mark4 = int(input("Enter the marks of Computer/Chemistry :"))
mark5 = int(input("Enter the marks of Physics :"))
mark6 = int(input("Enter the marks of Islamiat :"))

# calculating percentage of the person
obtained_marks = sum([mark1, mark2, mark3, mark4, mark5, mark6])
print(f"{obtained_marks}")
percentage = obtained_marks/total_marks*100

# Giving the grades for students by applying if elif condtion for student
if percentage <= 100 or percentage >= 90:
    print(f"Your Grade is \033[1mEx\033[0m with {percentage}%")  # Conditon for Grade Ex

elif percentage >= 80 and percentage < 90:
    print(f"Your Grade is \033[1mEx\033[0m with {percentage}%")  # Conditon for Grade A

elif percentage >= 70 and percentage < 80:
    print(f"Your Grade is \033[1mEx\033[0m with {percentage}%")  # Conditon for Grade B

elif percentage >= 60 and percentage < 70:
    print(f"Your Grade is \033[1mEx\033[0m with {percentage}%")  # Conditon for Grade C

elif percentage >= 50 and percentage < 60:
    print(f"Your Grade is \033[1mEx\033[0m with {percentage}%")  # Conditon for Grade D

else:
    print(f"Your Grade is \033[1mEx\033[0m with {percentage}%")  # Conditon for Grade f
