class Num():
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return len(self.n)

    def __str__(self):
        return str(self.n)


a = Num("Hussain")
b = Num(6)
c = Num(8)
d = Num(9)

print(a.__len__())
