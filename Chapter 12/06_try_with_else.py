# "else" with "try". When "try" runs along with "else" also runs. If "try" does not run, "else" also does not ru
# Finaly is a method that runs whether condition it is in try and exception. It is helpful in creating functions to print something after retun

def main():
    try:
        a = int(input("Enter a number: "))
        return a

    except Exception as e:
        return e

    finally:
        print("Hi, I am in finally")


print(main())
