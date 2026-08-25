"""
1. Create a class “Programmer” for storing information of few programmers
working at Microsoft.
"""


class Programmer():
    Salary = "$ 1,200,000"

    def __init__(self, name, language, exp, company):
        self.name = name
        self.language = language
        self.exp = exp
        self.company = company

    def info(self):
        info = f"Name: {self.name} \nLanguage: {self.language} \nExperience: {self.exp} years \nCompany: {self.company}"
        return info


# mustafa = Programmer("Mustafa", "Python", "3", "Google")
# print(mustafa.info())

Job_Data = [["Ali", "Python", "4", "Microsoft"],
         ["Hussain", "Python", "5", "Google"], 
["Abbas", "Java", "4", "Microsoft"],
["Haider", "C++", "5", "Google"], 
["John", "Php", "4", "Microsoft"],
["Mubashir", "Java", "5", "Google"], 
["Asif", "Python", "4", "Microsoft"],
["Danish", "HTML", "5", "Google"], 
["Zaki", "CSS", "4", "Microsoft"],
["Muneeb", "Python", "5", "Google"], 
["Riaz", "PHp", "4", "Microsoft"],
["Azam", "Swift", "5", "Google"], 
["Saim", "React", "4", "Microsoft"],
["Mehdi", "C#", "5", "Google"], 
["Amir", "Python", "4", "Microsoft"],
["Daniyal", "Python", "5", "Google"], 
]

for name, lan, exp, com in Job_Data:

    print(f"\033[1m{name}'s Data:\033[0m")
    print("*" * 40)
    name = Programmer(name.title(), lan, exp, com)
    print(name.info())
    print("-" * 40, end="\n\n")
