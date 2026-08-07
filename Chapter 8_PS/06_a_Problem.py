# Write a python function which converts inches to cms.
print(
    "                    \033[1mWelcome to the Centimeter to Inches  convertor!\033[0m")


def in_to_cm(cm1):
    inch = cm1 / 2.54
    inch_rounded = round(inch, 2)
    text = f"{cm1}\033[1mcm!\033[0m  equals to {inch_rounded}\033[1minches!\033[0m"
    return text


cm1 = float(input("Enter the value in centimeter: ",  ))
print(in_to_cm(cm1))
cm1 = float(input("\nEnter the value in centimeter: "))
print(in_to_cm(cm1))
cm1 = float(input("\nEnter the value in centimeter: "))
print(in_to_cm(cm1))
