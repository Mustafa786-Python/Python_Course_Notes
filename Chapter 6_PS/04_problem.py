'''Write a program to find whether a given username contains less than 10 
characters or not.'''
name = input("Enter an username: ")
#applying if and else condition
if len(name) > 10:
    print("The user name contians more than 10 characters: ")
elif len(name) == 10: 
    print("This user name contains 10 characters: ")
else: 
    print("The username contains less than 10 characters: ")
