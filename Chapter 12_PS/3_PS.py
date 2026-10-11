"""
3. Write a list comprehension to print a list which contains the multiplication table of a
user entered number.
"""
import csv


while True:
    try:
        num = int(input("Enter a number for mulplication: "))
        break

    except Exception as e:
        print("Only Integers")

num_list = [num * i for i in range(1, 10 + 1)]

try: 
    with open("table.csv", "r", encoding="utf8") as file:
        reader = csv.reader(file)

    for row in reader:
        print(row)

except:
     with open("table.csv", "w", encoding="utf8") as file:
            writer = csv.writer(file)
            writer.writerow(num_list)
    
        



