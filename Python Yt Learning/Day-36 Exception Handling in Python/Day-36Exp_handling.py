# #Day-36 Error Handeling or Exception Handling in Python
#Syntax in ''' '''
'''try:
     #statements which could generate 
     #exception
except:
     #Soloution of generated exception'''
# # Multiplication Table 
# a = input("Enter the Number : ")
# print(f"Multiplication table of {a} is : ")

# try:
#     for i in range (1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#     print("Invalid input!")


# print("some imp lines of code")

# print("End of Pro")

# Specific  Errors
try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
