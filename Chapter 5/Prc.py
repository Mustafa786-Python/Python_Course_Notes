from typing import Any
new_dict = dict(name="ALi", number=123, float=123.123, bolean=True)
print(new_dict, end="\n\n")

# thisdict1 = dict(brand="Ford", electic=False, year=1964,
#                  colors=["red", "white", "blue"])
# print(thisdict1, end="\n\n")
# thisdict = {
#     "brand": "Ford",
#     "electric": False,
#     "year": 1964,
#     "colors": ["red", "white", "blue"]
# }
# # print(thisdict)
# # print(type(thisdict["colors"]))
# print(new_dict.keys())
# print(thisdict.keys())
# print(new_dict.values())
# print(thisdict.values())
subjects = ("Apple", "Banana", 'oramge', 'tomoto')
dict1: dict[str, Any] = dict.fromkeys(subjects, True)
print(dict1.update({"Hussain":  False}))

print(dict1)
