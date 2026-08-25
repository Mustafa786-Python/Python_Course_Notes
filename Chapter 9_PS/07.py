with open("python_file.text", "r") as f:
    lines = f.readlines()



lines_lower = list(map(str.lower, lines))
# print(lines_lower)

word = 'python'
lines_list = []
lineno = 1


def loop():
    for num, line in enumerate(lines_lower):
        if word in line:
            lines_list.append(num)

    print(f"The word {word.title()} is in the line number {lines_list}")


if word in lines_lower:
    loop()
else:
    print("Not present")
