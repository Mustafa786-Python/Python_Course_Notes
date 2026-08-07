# Write a python function to remove a given word from a list ad strip it at the same time
def rem(l, word):
    n = []
    for item in l:
        if item != word:
            n.append(item.strip(word))
    return n


l = ["Harry", "Rohan", "Shubham"]
print(rem(l, "an"))
