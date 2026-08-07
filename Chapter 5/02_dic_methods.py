# Methods of dictionery
marks = {
    "Hussain": 50,
    "ALi": 60,
    "Boolean": True,
    "list1": [34, 565, 56, 32, 64],
    "tpl": (23, 45, 565, 565)
}

# Methods
# print(marks.items())  # it converts each key value into tuple
# print(marks.keys())  # Only returns keys of dic
# print(marks.values)  # It gives only values of key in dic
# It helps to update and insert new key value pair in the dic.
# marks.update({"Hussain": 100, "list2": [20, 40, 230, 45, 67]})
# print(marks)

# print(marks.get("Harry")) #It gives None when there is no such key in dic
# print(marks["Harry"]) #It gives error when there is no such key in dic

# print(marks.pop("ALi")) #it remvoves and return the key value in the dic
# print(marks)
# marks.clear() #It empty all dictionary
# print(marks)
# marks.update({"Hussain": 786, "List": [
#              12, 34, 56, 767], "Tpl": (12, 45, 556, 'Ali')})
# print(marks)
del marks["Hussain"]  # It works similar to pop
marks.pop("ALi")
# It returns the key if exist and if not exist create it and then returns
print(marks.setdefault('Ali', 89))
print(marks.setdefault('tpl'))
print(marks)

dic_2 = marks.copy()
del marks["Boolean"]
marks.pop('Ali')
print(marks)
