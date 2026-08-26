list1 = ['Python', 'Ali', 'Hussain']

listsmall = list(map(str.lower, list1))
print(listsmall)

if "python" in listsmall:
    print("Yes")
else:
    print("No")
