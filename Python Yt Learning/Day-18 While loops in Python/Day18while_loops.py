#while loops in Python
# i=0
# while(i<=3):
#     print(i)
#     i=i+1
# print("Done from the loop")

#take input from user
i = int(input("Enter the number :- "))
while(i<=3):
    i = int(input("Enter the number :"))
    print(i)
print("Done with the Loop ")

#decrementing while loop
count = 5
while (count > 0):
  print(count)
  count = count - 1

# Else with While Loop
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')

#do while loop in Python
while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break  #if number is +ve then loop never end ...
  
  