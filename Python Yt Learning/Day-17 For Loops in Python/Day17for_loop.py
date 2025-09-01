# For Loops in Python
# iterationg over a string
name = 'Ujjwal'
for i in name:
    print(i)
    if (i=="U"):
        print("This is special charcater ")


colors = ["Red","Green","Blue","Yellow"]

for color in colors:
    print(color)
    for i in color:
        print(i)


for j  in range(10):
    print(j+1)

for k in range(1,9):
    print(k)

for k in range(1,20001):
    print(k)



for k in range(1,12,3):
    print(k)   #prints 1 to 12 diiff 3 each digit 