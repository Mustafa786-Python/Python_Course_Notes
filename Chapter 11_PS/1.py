"""
Create a class (2-D vector) + use it to create another class representing a 3-D
vector.
"""


class Vector_2D:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    @property
    def show(self):
        print(f"The 2d vectors are {self.i}i + {self.j}j")


class Vector_3D(Vector_2D):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    @property
    def show(self):
        print(
            f"The 2d vectors are {self.i}i + {self.j}j + {self.k}k")


a = Vector_2D(3, 8)
a.show

b = Vector_3D(5, 9, 8)

b.show
