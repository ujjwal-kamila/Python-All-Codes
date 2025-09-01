# #  Python Lists
# l = [1,3,5,7]  #list declearation
# print(l)

marks = [5,7,"Ujjwal",True,8,9,10,12,15]
# print(marks)
# print(type(marks)) 
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

# print(marks[-3]) # Neg index
# print(marks[len(marks)-3]) # Positive index
# print(marks[4-3]) # Positive index
# print(marks[1]) # Positive index

if 7 in marks:
    print("Yes")
else:
    print("No")

#same things applies for strings as well 
if "ujw" in "Ujjwal":
    print("Yes")
else:
    print("No")


# print(marks) #prints all elem in marks 
# print(marks[:])  #prints all elem in marks 
# print(marks[1:-1])
# print(marks[1:8])
# print(marks[1:8:2])  #jump index is 2 so jump 2


lst = [i for i  in range(10)]
print(lst)  #print whole list


lst = [i*i for i  in range(10)]
print(lst)  #print whole list


lst = [i*i for i  in range(10) if i%2==0] # divisable by 2 Even numbers 
print(lst)  #print whole list