import random as rd 

a = rd.randint(1,10)
print(a)

b= rd.randrange(1,5)
print(b)

c= rd.random()
print(c)

d= rd.uniform(1,4)
print(d)

# create a list l 
list = [2,3,45,56,78,2,1,8]
list_elements = rd.choice(list)
print(list_elements)

# suffle the list
list1 = [2,87,45,10,78,12,18,88]
list_elements1 = rd.shuffle(list1)
print(list1)
