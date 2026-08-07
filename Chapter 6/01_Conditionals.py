age = int(input("Enter your age: "))
if age >= 18:
    print("\033[1m\"Congratulations!\"\033[0m You are an adulut")
elif age < 0:
    print("Invalid input")
elif age == 0:
    print("Your age can not be zero")
else:
    print("\"OOps\" You are not an adult")
