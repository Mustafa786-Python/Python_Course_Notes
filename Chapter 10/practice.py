"""
Inside the editor, complete the following steps:
Create a class called Person
Add an __init__ method that takes name and age as parameters
Add a method called greet that prints "Hello, my name is " followed by the name
Create an object p1 of the class with name "John" and age 36
Call the greet method on p1
"""


class Person():
    def __init__(self, name="someone", age=15):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and my age is {self.age}")


p1 = Person()
p1.greet()
