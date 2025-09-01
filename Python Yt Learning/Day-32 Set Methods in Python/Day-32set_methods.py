# Day-32 Set Methods in Python

s1= {1,2,5,6,7}
s2 = {3,6,7}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1,s2)

s1.update(s2) # put values from s2 in s1
print(s1,s2)

#sample example of union and update
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
#Prints union cities
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.update(cities2)
#Prints update cities
print(cities)

#intersection saple example
c1 = {"Kolkata", "Bihar", "Jhargram", "Delhi"}
c2 = {"Delhi", "Kolkata", "Medinipur", "Nadia"}
c3 = c1.intersection(c2)
#Prints intersection  cities
print(c3)

#symmetric_difference symmetric_difference_update()

c4 = {"Kolkata", "Bihar", "Jhargram", "Delhi"}
c5 = {"Delhi", "Kolkata", "Medinipur", "Nadia"}
c6 = c4.symmetric_difference(c5)  
# prints uncommon 
print(c6)


#intersection_update
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)

print(cities)


#difference and difference_updat
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}

cities3 = cities.difference(cities2) 
#prints only items that are only present in the original cities
print(cities3)


#difference_update() method updates into the existing set from another set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Berlin", "Kabul", "Delhi"}

print(cities.difference_update(cities2))


#Checks if all the items of a particular set are present in the original set and returns True if all the items are present else false
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

print(cities.isdisjoint(cities2))



# subset cheak
# Checks if all the items of a particular set are present in the original set
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)


#remove the chosen option
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Madrid")
print(cities)


#discard method
cities = {"Tokyo", "Madrid","Delhi"}
cities.discard("Madrid")
print(cities)


#pop method
cities = {"Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)


#del method for delet the wntire sets 
# cities = {"Tokyo", "Madrid","Delhi"}
# del cities
# print(cities) 


info = {"Carla",19,False,5.9}

if "Carla" in info:
    print("Carla is Present .")
else:
    print("Carla is not Present .")