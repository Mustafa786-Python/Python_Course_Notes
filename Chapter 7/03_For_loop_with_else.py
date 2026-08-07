# Practicing for loop with else.
name = "\tMustafa"
for i in name:
    print(i)
else:
    print("\tThe Loop is End")

sentence = input("Enter a sentence: ")
for a in sentence:
    print(a)
else:
    print("\nThe loop is end")

list1 = ["Ali", "Mustafa", "Danish", "Hussain", 786, 919]  # Printing list
for b in list1:
    print(b)
else:
    print("\nThe loop is end\n")

'Printing list with while loop'
c = 0
while c < len(list1):
    print(list1[c])
    c += 1
else:
    print("\nThe loop is end using while loop")
