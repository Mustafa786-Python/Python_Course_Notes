# Write a python function which converts inches to cms.
print("                    \033[1mWelcome to the Inches to Centimeter convertor!\033[0m")

def in_to_cm(inch):
    cm = inch * 2.54
    text = f"{inch}\033[1minches\033[0m equals to {cm:.3f}\033[1mcm\033[0m"
    return text

inch = float(input("Enter the value in inches: "))
print(in_to_cm(inch))
inch = float(input("\nEnter the value in inches: "))
print(in_to_cm(inch))
inch = float(input("\nEnter the value in inches: "))
print(in_to_cm(inch))
