#Break & Continue statement
for i in range(12):
  if(i == 10):
    break
    print("exit from the loop")
  print("5 X", i, "=", 5 * (i+1))

#continue statement
for i in range(12):
  if(i == 10):
    print("skip the iteration")
    continue
  print("5 X", i, "=", 5 * (i+1))


i = 0
while True:
  print(i)
  i = i + 1
  if(i%100 == 0):  #prints 0 to 100
    break

