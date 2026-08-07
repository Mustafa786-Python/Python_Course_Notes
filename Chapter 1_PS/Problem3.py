import os

# Select the folder you want to select
directory_path = '/New Folder'

# list the folders in the  os module 
contents = os.listdir(directory_path)

print(contents)