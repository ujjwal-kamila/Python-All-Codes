count=0
with open("file.txt",'r') as r:
    for i in r:
        count = count+1
print(count)
