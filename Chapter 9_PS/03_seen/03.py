def create_table(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n * i}\n"

    with open(f"03_seen/table{n}.txt", "w") as f:
        f.write(table)


for i in range(1, 21):
    create_table(i)
