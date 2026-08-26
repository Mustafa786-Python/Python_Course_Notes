"""
Super() is a builtin function that let a child class to access its parent's methods

"""


# class Employee:
#     def __init__(self):
#         print("Employee Constructor")
#     a = 10


# class Programmer(Employee):
#     def __init__(self):
#         super().__init__()
#         print("Programmer Constructor")
#     b = 10


# class Manager(Programmer):
#     def __init__(self):
#         super().__init__()
#         print("Manager Constructor")
#     c = 15


# o = Manager()
# print(o.a)


#Another Example:

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        print(f"{self.name} earns Rs {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, size ):
        super().__init__(name, salary)
        self.size = size

    def get_info(self):
        super().get_info()
        print(f"The Team Size is {self.size}")

a = Manager("Mustafa", "10,000,000", "10")
a.get_info()
        
