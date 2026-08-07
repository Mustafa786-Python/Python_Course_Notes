# # # using break statement
# # for i in range(100):
# #     if i == 50:
# #         break  # It stops the the loop when the given condition is true
# #     print(i)

# list1 = ["Ali", "Mustafa", "Danish", "Hussain", 786, 919]
# # for i in list1:
# #     if i == 786:
# #         break
# #     print(i)
# #Using while loop
# num = 0
# while num < len(list1):
#     if list1[num] == 786:
#         # num += 1
#         break
#     print(list1[num])
#     num += 1
# t = (45, 678, 75, 1343, 34)
# num = 0
# while num < len(t):
#     if t[num] == 75:
#         break
#     print(t[num])
#     num += 1


'Using Continue'
for i in range(10):
    if i == 7:
        continue  # It stops the the loop when the given condition is true
    print(i)

list1 = ["Ali", "Mustafa", "Danish", "Hussain", 786, 919]
for i in list1:
    if i == 786:
        continue
    print(i)

t = (45, 678, 75, 1343, 34)
num = 0
while num < len(t):
    if t[num] == 75:
        continue
    print(f"{t[num]}")
    num += 1
