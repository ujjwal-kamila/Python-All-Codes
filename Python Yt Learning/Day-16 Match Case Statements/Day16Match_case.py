 # Matchcase  and switch case 
 #the below code only works in python 3.10
# x = int(input("Enter the value of x: "))
x = 80

match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is 4")
    case _ if x != 10:
        print(f"{x} is not  10")
    case _ if x != 20:
        print(f"{x} is not  20")
    case _:
        print(x)
        
