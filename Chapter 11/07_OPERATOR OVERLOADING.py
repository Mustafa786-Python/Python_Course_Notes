class Num():
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

    # def __str__(self):
    #     return str(self.n)


a = Num("Hussain")
b = Num(6)
c = Num(8)
d = Num(9)

print(b + c)
