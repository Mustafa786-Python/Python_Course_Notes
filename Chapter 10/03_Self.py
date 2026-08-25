# Self Parameter:
"""
It is an instance of class. It is automatically passed by calling a function
"""


class Employee:
    name = "someone"  # Class attribute
    language = "Python"  # Class attribute
    salary = "Rs 1,200,000"  # Class attribute

    def getinfo(self):
        print(
            f"His name is {self.name.title()}. He is learning {self.language} programming language. His salary is {self.salary}", end="\n\n")

    @staticmethod #It is a decorator, we use it when we do not need parameter. 
    def info():
        print("You are Champion!", end="\n\n")


mustafa = Employee()
mustafa.name = "mustafa"

print("method 1")
mustafa.getinfo()  # call method 1

print("method 2")
Employee.getinfo(mustafa)  # call method 2

mustafa.info()
