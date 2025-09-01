#Day-32 Dictionary methods
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

# ep1.update(ep2)  # for update with another dict
# ep1.clear()  #for clear the whole dict
# ep1.pop(122) #delet the item 

ep1.popitem()  #delet the last item 
del ep1[122] 
print(ep1)