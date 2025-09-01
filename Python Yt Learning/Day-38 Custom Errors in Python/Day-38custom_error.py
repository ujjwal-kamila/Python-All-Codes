#Day-38 Custom Errors in Python

# # Value errors 
# a = int(input("Enter any value between 5 and 20 :"))

# if(a<5 or a>20):
#     raise ValueError("Value should be in between 5 and 20")


# Exercise 
a = int(input("Enter any value between 5 and 9 : "))

if(a == "quit"):
    print("quit")
elif(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")

#Raising Custom errors / value errors
salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")

# Defining Custom Exceptions
class CustomError(Exception):
 ''' # code ...
  pass

try:
  # code ...

except CustomError:
  # code...'''
