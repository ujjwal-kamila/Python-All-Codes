marks = [3, 5, 7, "Rudra", 123, 456, 15, 95, 53]
print(marks)
print(marks[3])
print(marks[-3])
print(marks[len(marks)-3])

if 5 in marks:
    print("yes")
else:
    print("no")
    
print(marks[3:])
print(marks[1:5])
print(marks[1:5:2])
print(marks[1::2])

lst = [i * i for i in range(9)]
print(lst)
lst = [i * i for i in range(9) if i%2==0]
print(lst)