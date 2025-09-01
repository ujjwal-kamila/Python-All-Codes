# Functions in Python

def calculateGmean(a, b):
  mean = (a*b)/(a+b)   #fun defination
  print(mean)

def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

def isLesser(a, b):
  pass  # use pass to avoid error for incomplete functions
  

a = 9
b = 8
isGreater(a, b)   #fun call
calculateGmean(a, b)   #fun call
# gmean1 = (a*b)/(a+b)
# print(gmean1)
c = 8
d = 74
isGreater(c, d)
calculateGmean(c, d)

# gmean2 = (c*d)/(c+d)
# print(gmean2)