# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour.

import time
t = time.strftime('%H:%M:%S')
print(t)
t = int(time.strftime('%H'))

if(t>=0 and t<12):
  print("Good Morning")

elif(t==18):
    if(t>=18 and t>22):
      print("Good Evening")
    elif(t>=22 and t>=0):
      print("Good Night")
    else:
      print("Good Night")
else:
  print("Good Afternoon")


# Another input
import time
t = time.strftime('%H:%M:%S') 
hour = int(time.strftime('%H'))
# hour = int(input("Enter hour: "))
# print(hour)

if(hour>=0 and hour<12):
  print("Good Morning Sir!")
elif(hour>=12 and hour<17):
  print("Good Afternoon Sir!")
elif(hour>=17 and hour<0):
  print("Good Night Sir!")