#Day-49 File Operations In Python

#File operations in Python 
# Opening a File
## f = open('myfile.txt', 'r')

# READING A FILE

# f = open('myfile.txt', 'r')
# # print(f)
# text = f.read()
# print(text)
# f.close()

# WRITING A FILE

f = open('myfile.txt', 'a')
f.write('Hello, world!')
#Closing a File
f.close()

# The 'with' statement
with open('myfile.txt', 'a') as f:
  f.write("Hey I am inside with")