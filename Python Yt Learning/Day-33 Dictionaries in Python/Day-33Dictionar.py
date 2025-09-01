# Day-33 Dictionaries in Python
# syntax 
# dic = {
#     "Ujjwal" : "Human being ",
#     "Book": "Object"
# }
# print(dic["Ujjwal"])

info = {'name':'Ujjwal','age':19 ,'eligible':True}
print(info)

#Acessing single values 
print(info['name'])
print(info.get('eligible'))

#Acessing Multiple values 
print(info.values())


for key in info.keys():
  print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}") 

# #Acessing keys 
# info = {'name':'Ujjwal', 'age':19, 'eligible':True}

# print(info.keys())
# #Accessing key-value pairs
# info = {'name':'Ujjwal', 'age':19, 'eligible':True}

# print(info.items())