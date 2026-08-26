

class Employee:
    a = 5


class Programmer(Employee):
    b = 10


class Manager(Programmer):
    c = 15


o = Employee()
print(o.a)
# print(o.b) # Gives Erro: Because Employee class does not contain b

o = Manager()
print(o.a)
print(o.b)
print(o.c)
