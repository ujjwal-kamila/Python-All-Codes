# Type  casting : in built in functions 
# int(), float(), hex(), oct(), str(), etc .

a = "1"
b = "2"
print(a+b) #a & b are known as str so a+b =12
# convert type

print(int(a)+int(b)) # out : 3
#type converstion
c = 1.9
d =8
print(c+d)

#Example of explicit typecasting:
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)


#Example of implicit type casting:
# Python automatically converts
# x to int
x = 7
print(type(x))
 
# Python automatically converts y to float
y = 3.0
print(type(y))
 
# Python automatically converts z to float as it is x float addition
z = x + y
print(z)
#type of z
print(type(z))