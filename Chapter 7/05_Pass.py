"Pass Satatement"  # It is a nul statement in python. It tell the program to do nothing
# it is used when we  do not want to work on the loop now but we want to to use the loop in the future. At that moment we use pass satetment to tell our program to do nothing
l = [56, 784, 232]
for i in l:
    pass
print("The for loop is skipped")
num = 0
while num < len(l):
    print(l[num])
    num += 1
print("The while loop result")

"Change the the condition"
g = [56, 784, 232]
for i in g:
    print(i)
print("The for loop's reseult")
num = 0
while num < len(g):
    pass

print("The while loop is skipped")