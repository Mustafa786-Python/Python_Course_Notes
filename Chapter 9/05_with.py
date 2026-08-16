"With Statement"
#This helps us to make close a program in file wihthout using the burden of close f.
#Example:
f = open("file.txt")
print(f.read())
f.close()

#similar as:
with open("file.txt") as f:
    print(f.read())
