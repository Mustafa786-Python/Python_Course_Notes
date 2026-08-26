"@classmethod is a decorator which is bounds with class not the object of the class"
"cls intead of self parameter"


class Employee:
    a = 1

    @classmethod
    def info(cls):
        print(f"The value of a is {cls.a}")


obj = Employee()
obj.a = 45
obj.info()
