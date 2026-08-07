#Identify Spam folders
p1 = "Make a lot of money"
p2 = "buy Now"
p3 = "subscribe this"
p4 = "click here"

inp = input("Enter the sentence: ") #Taking input form the user

if ((p1 in inp) or  (p2 in inp) or (p3 in inp) or (p4 in inp) or ()):
    print(f"Alert! This is a spam message")
else: 
    print(f"No, the comment is not a spam") 

