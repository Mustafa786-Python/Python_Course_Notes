from math import pi, exp2

# def http_servor(status):
#     match status:
#         case 400:
#             return "I am good"

#         case 404:
#             return "Error 404"

#         case 500:
#             return "You are amazing"

#         case _:
#             return "Uknown Servor"


# print(http_servor(501))

class Circle:
    def __init__(self, radius):
        self.radius = radius


class Square:
    def __init__(self, side):
        self.side = side


def area(shape):
    match shape:
        case Circle(radius=r):
            return round(pi * exp2(r))

        case Square(side=s):
            return round(exp2(s))


print(area(Circle(20)))
print(area(Square(20)))
