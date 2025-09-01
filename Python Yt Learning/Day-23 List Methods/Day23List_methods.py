l = [1,2,4,6,8,1]
# print(l)
# # To add elemtns in list append.(element)
# l.append(7)
# print(l)
# # To sort elements in assending order 
# l.sort()
# print(l)
# l.sort(reverse=True)#for decending order use 
# print(l)
# #Reverse method
# l.reverse()
# print(l)
# print(l.index(1))  # print where is the index 
# print(l.count(1))  #count the 1
# m = l  #take m as list
# m[0] = 0   #put 0 in the  0th index 
# print(l)   #but here l changes 
# That's why we not use the upper condition
#We use the lower copy method for new m list :
# m = l.copy()  #take m as list
# m[0] = 0   #put 0 in the  0th index 
# print(l) 
# print(m) # create m as list and l remain same 
# #insert in index 
# l.insert(1,100)  # put 100 ib 1th index
# print(l)  

m = [100,200,500]
k = l+m

print(k) # take a new list 

# l.extend(m) #add m list to l list
print(l) # l remain same