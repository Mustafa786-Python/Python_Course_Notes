"""
Create a class ‘Employee’ and add salary and increment properties to it.
Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 
which changes the value of increment based on the salary
"""


class Employee:
    def __init__(self, salary):
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, amount):
        if amount > 100000:
            raise ValueError("No more than Rs 100, 000")

        if amount < 25000:
            raise ValueError("The salary should be larger then 25000")

        self._salary = amount


a = Employee(30000)
print(a.salary)
