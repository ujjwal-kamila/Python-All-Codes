# Day-48 Local and Global variables in Python
#local vs global variables
#example 5 is local variable and 4 is global variable

# local variable destroyed when function returns 

# global variable defined outside and is accessible from within an funcion in your code
# x = 4 # here x is global 
# print(x)

# def hello():
#     x= 5  # in that func x is local variable
#     print(f"The Local x is : {x}")
#     print("Hello Ujjwal")
    
# print(f"The Global x is : {x}")   
# hello()
# print(f"The Global x is : {x}")   

x = 10  # global variable


def my_function():
  global x  #take global x and changed it to 5 in next line
  x = 5  # this will change the value of the global variable x
  y = 5  # local variable


my_function()
print(x)   # prints 5
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function