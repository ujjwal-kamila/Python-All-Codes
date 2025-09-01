# if else elif conditional statements 
a = int(input("Enter Your Age : "))   #take age as input

#condiotional operators
# < , > , >= , <= ,!= , ==
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)

if(a>=18):  #condition
    print("You can drive :)")  #indetation must be do carefully
else:
    print("You can't drive:( ")
print("Yay!")  #prints always  for no indentation

#if else elif conditions
applePrice = 10
budgetPrice = 200
if (budgetPrice-applePrice >50):
    print("Alexa, add 1kg Apples to the cart :)")
elif (budgetPrice-applePrice >70):
    print("It's ok You can Buy")
else:
    print("Alexa, do not dd Apples to the cart")



#another if else elif uses
num = int(input("Enter the value of num: "))
if (num <0):
    print("Numbr is negative ")
elif(num == 0):
    print("Number is Zero ")
else:
    print("Number is Positive")


#Nested if Else Statements:
numb = 18

if(numb < 0 ):
    print("Number is Negative")
elif(numb > 0):
    if (numb <= 10):
        print("Number is between 1-10 ")
    elif(numb > 10 and numb <=20):
        print("Number is between 10-20 ")
    else:
        print("Number is Greater then 20")
else:
    print("Number is Zero")