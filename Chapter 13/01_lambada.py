def a(x): return x**2


print(a(3), end="\n\n")

"Practice"
"""def add(a, b):
    return a + b"""


def b(a, b): return a + b


print(b(5, 10), end="\n\n")

"""def is_even(number):
    return number % 2 == 0"""


def c(number): return number % 2 == 0


print(c(3))
print(c(10), end="\n\n")


"""
def maximum(a, b):
    if a > b:
        return a
    else:
        return b

"""


def d(a, b): return a if a > b else b


print(d(3, 5))
print(d(10, 0), end="\n\n")

"""
def discounted_price(price, discount):
    return price - (price * discount / 100)

"""
e = lambda price, discount: price - (price * discount / 100)
print(e(1000, 20), end="\n\n")

