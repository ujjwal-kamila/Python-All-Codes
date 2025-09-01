#Day-44 How Import Works in Python
# How import works on python 
#using the name of module.
# import pandas as pd
# pd.read_csv() # for read in csv file


# import math 
# result = math.sqrt(9)
# print(result)   # output will be 3,

# if we return one fun "sqrt"
from math import sqrt,pi
result = sqrt(9) * pi 
print(result)

#As keyword
import math as m
result = m.sqrt(9) * m.pi
print(result)

# To see the dictonary of math fun
import math
print(dir(math))
print(math.nan , type(math.nan))  # nan <class 'float>
print() # this is a new line

from Day44import import welcome,ujjwal
welcome()
print(ujjwal)

print() # this is a new line

import Day44import as dy
dy.welcome()
print(dy.ujjwal)


