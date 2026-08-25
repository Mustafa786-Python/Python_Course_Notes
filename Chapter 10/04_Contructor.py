
class Employee:
    # name = "someone"  # Class attribute
    # language = "Python"  # Class attribute
    # salary = "Rs 1,200,000"  # Class attribute

    def __init__(self, name, language, salary):  # Dunder method which is automatically called
        self.name = name
        self.langauge = language
        self.salary = salary

        print("You are champion")

    def getinfo(self):
        print(
            f"His name is {self.name.title()}. He is learning {self.langauge} programming language. His salary is {self.salary}", end="\n\n")


mustafa = Employee("Mustafa", "Python", f"Rs 1,200,000")
# mustafa.name = "mustafa"
mustafa.getinfo()

ali = Employee("Ali", "Javascript", f"Rs 1,400,000")
ali.getinfo()
