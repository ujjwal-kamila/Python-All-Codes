#Tuples opeartions
tuple1 = (0,8,3,2,3,2,4,5,3,6,7,3,5)
# res = tuple1.count(3)   #count 3 in the tuple
# res = tuple1.index(3)  # return the index of num

res = tuple1.index(3,5,9)   #index of 3 between 4-to-8 th index
# res = len(tuple1)
print('Count of 3 in tuple 1 is :',res)

# Manipulating Tuples

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)

temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

#add two tuples
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")  # tuple 1
countries2 = ("Vietnam", "India", "China")                           # tuple 2
southEastAsia = countries + countries2

print(southEastAsia)