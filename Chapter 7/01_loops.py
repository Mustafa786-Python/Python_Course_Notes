# List containing elements of different Python data types
mixed_values = [
    42,                     # int
    3.14,                   # float
    "hello",                # str
    True,                   # bool
    None,                   # NoneType
    [1, 2, 3],              # list
    (1, 2, 3),              # tuple
    {"a": 1, "b": 2},       # dict
    {1, 2, 3},              # set
    2 + 3j,                 # complex
    b"bytes",               # bytes
    bytearray(b"abc"),      # bytearray
    frozenset({1, 2, 3}),   # frozenset
    range(5),               # range
    lambda x: x * x,        # function (lambda)
    Exception("error"),     # Exception object
]

i = 0
while (i < len(mixed_values)):
    print(mixed_values[i])
    i += 1

print(f'\n')

# By using for loop
for l in mixed_values:
    print({l})
    