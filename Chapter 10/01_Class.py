"""
Class is a blue print for creating objects. For example class is form, when it is filled it is object. Means from a form we can fill multiple information of the people. Similary from a class we can create multiple objects.
Class contains information to create valid objects.
"""
"Class attribute are those which are derived from a class"
"Object attributes or Instant Attributes are created seperately as shown in exampl or e"


class Employee:
    name = "Harry" # Class attribute
    language = "Py"  # Class attribute
    salary = "1, 200, 000" # Class attribute


harry = Employee()
harry.name = "Harry"  # Object Attribute or instant attributes
print(f"{harry.salary} \n{harry.language}\n {harry.name}")  

mustafa = Employee()
mustafa.name = "Mustafa"  # Object Attribute or instant attributes

print(f"{mustafa.name} \n{mustafa.salary} \n{mustafa.language} ")
