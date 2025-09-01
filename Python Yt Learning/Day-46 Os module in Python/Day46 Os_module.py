# Day-46 Os module in Python

#to create 1-100 folders 
# import os
# if(not os.path.exists("data")):
#     os.mkdir("Python") # create a folder name  "Python"

# for i in range (0,100):
#     os.mkdir(f"Python/Day-{i+1}") #create 1-100folders in python

# to print the folders 
import os 
folders = os.listdir("Python")
print(folders)

#to rename os.rename

#prints indivusal folders
for folder in folders:
    print(folder)

#prints folders and their files
for folder in folders:
    print(folder)
    print(os.listdir(f"Python/{folder}"))


    
print(os.getcwd())
