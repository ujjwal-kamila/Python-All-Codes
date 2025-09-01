# List Tuples  
tup = (1,3,5,8,"Raj",True,3421)
print(type(tup),tup)
print(len(tup))
# positive index
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[5])
# print(tup[15])  # through error bcs the 15th index is not here 
# negative index
print(tup[-1])
print(tup[-4])

#sample tuple 
tuple1 = (1,2,2,3,5,4,6)

tuple2 = ("Red", "Green", "Blue")

print(tuple1)

print(tuple2)

if  3421 in tup:
  print("Yes 3421 is present in this tuple")
  
tup2 = tup[1:4]
print(tup2)