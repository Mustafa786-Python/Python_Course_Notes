"The global keywords helps us in function to modify the global variable"

a = 10


def func():
    global a
    a = 9
    print(a)


func()
print(a)
