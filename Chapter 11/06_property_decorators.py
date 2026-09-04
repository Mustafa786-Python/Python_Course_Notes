class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The value of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.enamename = value
        self.fname = value.spilt(" ")[0]
        self.lname = value.spilt(" ")[1]


e = Employee()

print(e.a)

e.name = "Mustafa Ali"
print(e.lname, e.fname)
e.show()
