import random
nums = {12, 45, 5654, 5464, 645, 455, 455, 455}  # This is a set.random()
# nums1 = set()
# for i in range(15):
#     a = random.randint(50, 100)  # Generates a random integer between 1 and 100
#     nums1.add(a)
# print(nums1, type(nums1))
# nums1.clear()
# print(nums1, type(nums1))

# "Methods"
# # print(nums.pop()) It returns and removes an item in the set radomly
# # print(nums.pop())

# # It counts the length of the set
# print(f"The length of the list: {len(nums)}")
# nums.remove(645)
# nums.clear()
# print(nums)

set1 = {5, 10, 15, 20, 25}
set2 = {5, 10, 15}
# It checks if set2 is subset of set1. Small part of bigger one
print(set1.issubset(set2))
# It checks if set2 is superset of set1. Bigger part containing smaller one
print(set1.issuperset(set2))

print(set2.issubset(set1))  # It checks if set1 is superset of set2
print(set2.issuperset(set1))
set3 = set1 | set2
set4 = set1.union(set2)
set5 = set1.update(set2)
print(f"The addition of set by \'|\'{set3}")
print(f"The addition of set by \'.union()\'{set4}")
print(f"The addition of set by \'.update()\'{set4}")
