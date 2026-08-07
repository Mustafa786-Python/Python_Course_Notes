mixed_tuple = (
    42,                  # int
    3.14,                # float
    "Python",            # str
    True,                # bool
    None,                # NoneType
    42,                  # repeated int (for count)
    "AI",                # str
    2.718,               # float (e ≈ 2.718)
    False,               # bool
    (1, 2),              # nested tuple
    "Python",            # repeated str (for count)
    100,                 # int
    3.14,                # repeated float (for count)
    True,                # repeated bool (for count)
    None,                # repeated None (for count)
    "Machine Learning",  # str
    42,                  # repeated again!
    0.0,                 # float
    (3, 4, 5),           # nested tuple
    "Data Science"       # str
)

"Functions on Tuple"
length = len(mixed_tuple)
python = mixed_tuple.count("Python")
index = mixed_tuple.index(True)
none = mixed_tuple.count(None)
n42 = mixed_tuple.count(42)
data = f"""
- \033[1mTotal items:\033[0m    {length}
- \033[1mPython repeats:\033[0m {python}
- \033[1mIndex of True: \033[0m {index}
- \033[1mNone repeats:  \033[0m {none}
- \033[1m42 repeats:    \033[0m {n42}
"""
print(data)
print(print(mixed_tuple[1::5])) 
