"Write a program to mine a log file and find out whether it contains ‘python’."
print()
with open("python_file.text", "r") as f:
    content = f.read()


if "Python" in content.lower():
    print("Yes, It contains ")
else:
    print("No, It does not contains")