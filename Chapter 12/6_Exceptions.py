while True:
    try:
        a = int(input(("Enter a number: ")))
        print(a)
        break

    except ValueError:
        print("Only numbers")
