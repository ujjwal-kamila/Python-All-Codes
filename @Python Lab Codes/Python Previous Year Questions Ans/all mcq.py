# Find output
data = [x for x in range (5)]
temp = [x for x in range(7)
        if x in data and x%2 == 0]
print(temp)


# What is the output of the following program?
T = (1, 2, 3, 4, 5, 6, 7, 8) 
print(T[T[T[ 6]-3 ]-6])


D = dict() 
for i in range (3): 
    for j in range(2): 
        D[i] = j 
print(D)

# tuple= (1, 2, 3, 4) 
# tuple.append( (5, 6, 7)) 
# print(len(my_tuple))
# Ans : Compilation Error

tuple= (1, 2, 3) 
print(2 * tuple)

list= [1, 2, 3, None, (1, 2, 3, 4, 5), ['G', 'for', 'A']] 
print(len(list))

list= ['python', 'learning', '@', 'A', 'for', 'abc'] 
print(list[ ::-2])

t=(1,2) 
print(2 * t)