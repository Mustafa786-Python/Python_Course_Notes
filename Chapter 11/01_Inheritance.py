"Inheritance lets one class (child) to take attributes from another class(parent)"


class Employee:
    company = "ABC company"
    name = "Zxy"

    def show(self):
        print(f"Mr. {self.name}, is in company {self.company}")


class Coder:
    language = "Python"

    def progamming_language(self):
        print(f"He is master in {self.language}")


class Programmer(Employee, Coder):
    company = "Google"

    def show_language(self):
        print(
            f"{self.name} has mastered {self.language}. He is working in {self.company}")


a = Programmer()

a.show()
a.progamming_language()
a.show_language()
