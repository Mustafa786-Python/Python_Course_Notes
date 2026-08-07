# In this less I learnt about Union and Intersection
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# print(cities.union(cities2))
# print(cities.intersection(cities2))
# # print(cities.pop())
# print(
#     f"From the set1 \"{cities.pop()}\" is removed. The remaing items are {cities}")
# print(
#     f"From the set2 \"{cities2.pop()}\" is removed. The remaing items are {cities2}")
# print(f"The union of both set are {cities.union(cities2)}")
# print(f"The intersection of both set are/is {cities.intersection(cities2)}")
cities.add("Karachi")
cities.add("Islamabad")
cities.add("Tehran")
cities.add("Gilgit City")
cities.add("Skardu")
cities2.add("Karachi")
cities2.add("Islamabad")
cities2.add("Tehran")
cities2.add("Gilgit City")
cities2.add("Skardu")
cities2.add("Moscow")
cities2.add("Karachi")
# print(cities)
# print(cities2)
uni = cities.union(cities2)
int2 = cities2.intersection(cities)
print(f"Items Union {uni}. The items length {len(uni)}")
print(f"Items Intersection {int2}. The items length {len(int2)}")

