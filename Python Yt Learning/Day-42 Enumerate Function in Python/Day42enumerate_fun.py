#Day-42 Enumerate Function in Python
# Storemarks out of 100
marks = [55,78,97,32,56,72,1,90]


'''
index = 0
for mark in marks:
    print(mark)
    if (index == 3):
        print("Ujjwal")
    index +=1
'''


# Using Enumarate Function store marks in index
for index , mark in enumerate(marks):
    print(mark)
    if (index == 3):
        print("Ujjwal :) ")


for index , mark in enumerate(marks):
    print(mark)
    if (index == 3):
        print("Ujjwal :) ")
