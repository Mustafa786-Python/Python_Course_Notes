# Write a program using functions to find greatest of three numbers.
def greatest(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(f"{num1} is the greatest")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} is the greatest")
    else:
        print(f"{num3} is the greatest")


# greatest(5, 6, 7)
# greatest(10, 6, 7)
# greatest(5, 15, 7)

# By using return function
def greatest1(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        text = f"{num1} is the greatest"
        return text
    elif num2 > num1 and num2 > num3:
        text = f"{num2} is the greatest"
        return text
    else:
        text = f"{num3} is the greatest"
        return text


print(greatest1(23, 45, 3))
