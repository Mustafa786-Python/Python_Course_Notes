from typing import Union, Tuple, List, Dict, Set

n: int = 5
name: str = "Harry"


def sum(a: int, b: int) -> int:
    return a + b


print(sum(5, 10))

#It is list of integers
numbers: List[int] = [1, 2, 3, 4, 5] 
print(numbers)

#It is tuple of integers
person: Tuple[str, int] = ("Ali", 5)
print(person)

#Dictionary with string keys and integer values
books: Dict[str, int] = {"Atomic Habits": 450, "Rich Dad Poor Dad": 300, "Quran": 20000}
print(books)

#Union for multiple types:
identifyer: Union[str, int] = "ali123"
print(identifyer)
