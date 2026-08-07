"""
Write a program to greet all the person names stored in a list ‘l’ and which starts 
with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]
"""
l = ["Harry", "Shabbir", "Sher", "Rahul"]
for i in l:
    if "S" in i:
        print(f"Assalmualikum! {i}")
    else:
        print(i)
print("\n")


"Harry Version"
for name in l:
    if (name.startswith("S")):
        print(f"Hello {name}")