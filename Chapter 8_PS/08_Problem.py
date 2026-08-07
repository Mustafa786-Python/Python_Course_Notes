# Write a python function to print multiplication table of a given number.
def table(num):
    print("Note: Only put numbers")
    for i in range(1, 10+1):
        mul = num * i
        print(f"{num} x {i} = {mul}")
    print("")


table(1.23)
table(46)
