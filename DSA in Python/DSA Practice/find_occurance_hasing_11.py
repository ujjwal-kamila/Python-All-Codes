# Find Occurance using hashing

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,9,5,67,2]

# using hash_list
hash_list = [0] * 11
for num in n:
    hash_list[num]+= 1
    
for num in m:
    print(f"{num}",end = ' -- ')
    if num<1 or num>10:
        print(0)
    else:
        print(hash_list[num])
print()
        
        
# Another Approach using dict
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,9,5,67,2]

freq_map = {}
for i in range(0, len(n)):
    if n[i] in freq_map:
        freq_map[n[i]]+=1
    else:
        freq_map[n[i]]= 1
print(freq_map)

for val in m:
    print(f"{val} -- {freq_map.get(val,0)}")