import os

# with open("file1.txt", "w"):
#     pass

with (
    open("file1.txt", 'r') as f1,
    open("file2.txt", 'w') as f2
):

    data = f1.read()
    write1 = f2.write(data)

f1.close()
f2.close

try:
    os.remove("file1.txt")
    os.remove("file2.txt")

except FileNotFoundError:
    print("File not found try again")
