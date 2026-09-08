"""
. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from 
‘Pets’. Add a method ‘bark’ to class ‘Dog’.
"""


class Animals:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def show(self):
        return f"""
Name: {self.name}
category: {self.category}
"""


class Pets(Animals):
    def __init__(self, name, category, owner):
        super().__init__(name, category)
        self.owner = owner

    def show(self):
        return super().show() + f"""Owner: {self.owner}
"""


class Dog(Pets):
    def __init__(self, name, category, owner, dog_type):
        super().__init__(name, category, owner)
        self.dog_type = dog_type

    def show(self):
        return super().show() + f"""Dog Type: {self.dog_type}
"""

    @staticmethod
    def bark():
        return "Bark!, Bark!"


a = Animals("Tom", "Pet Animal")
print(a.show())

b = Pets("Tom", "Pet Animal", "John")
print(b.show())

c = Dog("Tom", "Pet Animal", "John", "Norwegian Lundehund")
print(c.show())
print(c.bark())
