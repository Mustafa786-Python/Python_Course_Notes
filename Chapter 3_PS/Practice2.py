# Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
import datetime
name = input("Enetr your name: ")
date = datetime.datetime.now().strftime("%B %d,%Y") #%B for date, %d for month name, %Y for year
foramt = f"""
___________________________
Dear {name.title()},       
You are selected!           
{date}                     
___________________________
"""
print(foramt)
