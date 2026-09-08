"""
Write a class ‘Complex’ to represent complex numbers, along with overloaded 
operators ‘+’ and ‘*’ which adds and multiplies them.
"""


class Complex:
    
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        real_sum = self.real + other.real
        img_sum = self.img + other.img

        return Complex(real_sum, img_sum)
    # f"({self.real} + {other.real}) + ({self.img} + {other.img}) = {real_sum}  + {img_sum}i"

    def __mul__(self, other):
        real_mul = (self.real * other.real) - (self.img * other.img)
        img_mul = (self.real * other.img) + (self.img + other.real)
        return Complex(real_mul, img_mul)
    # f"({self.real} + {self.img}i) x ({other.real} + {other.img}i) = {real_mul} +  {img_mul}i"

    def __str__(self):
        if self.img < 0:
            return f"{self.real} - {-self.img}i"
        return f"{self.real} + {self.img}i"
        
    
a = Complex(10, 9)
b = Complex(5, 9)

print()
com_sum = a + b
com_mul = a * b

print(f"{a} x {a} = {com_mul}")
print(f"{a} + {a} = {com_sum}")
