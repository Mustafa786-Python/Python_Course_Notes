class Employee:
    name = "Harry"  # Class attribute
    language = "Py"  # Class attribute
    salary = "Rs 1,200,000"  # Class attribute


mustafa = Employee()
mustafa.language = "Java"  # Object Attribute or instant attribute
print(f"{mustafa.salary} \n{mustafa.language} ")


#Conept
"First the interpretor sees instant attributes, if it is not present it see class attributes"