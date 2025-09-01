# # Functions Arguments 
# pass arguments and bulk arguments

#required argumments
def average(a,b):
    print("The average is : ",(a+b)/2)
average(1,5)

#default arguments
def average(a=5,b=4):
    print("The average is : ",(a+b)/2)
average(4) # takes that a=4 and b remain same returns 4 as avg



#default arguments
def average(a=10,b=12):
    print("The average is : ",(a+b)/2)
average(b=4) # takes that b=4 and b remain same returns 7 as avg



#default arguments 
def name(fname, mname = "kumar", lname = "Kamila"):
    print("Hello,", fname, mname, lname)
name("Ujjwal")


# keyword arguments
def name(fname, mname, lname):
    print("Hii,", fname, mname, lname)

name(mname = "Kumar", lname = "Kamila", fname = "Ujjwal")


#required argumments
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)
# name("ujjwal", "kamila")  #Through Error


#required argumments
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name("ujjwal", "kumar", "kamila")


#Variable-length arguments:
def name(*name):
    print("Hii,", name[0], name[1], name[2])
name("Ujjwal", "Kumar", "kamila")



# def average(a, b, c=1):
#   print("The average is ", (a + b + c) / 2) 


def average(*numbers):
  # print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
    # print("Average is: ", sum / len(numbers))
  return sum / len(numbers)

# average(4, 6)
# average(b=9)

c=average(1,2,3)
print(c)


# def name(**name):
#   # print(type(name))  #take dictionary
#   print("Hello,", name["fname"], name["mname"], name["lname"])


# name(mname="Buchanan", lname="Barnes", fname="James")





