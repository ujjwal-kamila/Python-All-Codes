#Day-51 seek() and tell() functions


with open ('file.txt','r') as f:
    print(type(f))
    #move to the 10th byte of the file
    f.seek(10)
    #read the next 5 bytes
    data = f.read(7)
    print(data)
    
    
    
with open('sample.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5)  #only 5 char from first
  
  
with open('sample.txt', 'r') as f:
  print(f.read())