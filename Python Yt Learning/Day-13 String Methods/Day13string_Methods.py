# Strings are immutable
a = "!!!Ujjwal!! !!!!!!!!!Ujjwal"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Ujjwal", "Raj"))
print(a.split(" "))
blogHeading = "introduction to jS"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Ujjwal"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))   #True
print(str1.endswith("to", 4, 11))   #False


str1 = "He's name is Rahul. He is an honest man."
print(str1.find("is"))  #returns 10 as position 
print(str1.find("ishh")) #retruns -1
#print(str1.index("ishh"))  #throw error!

str1 = "WelcomeToTheConsole"
print(str1.isalnum()) # alphanumaric "A" to "Z" "a" to "z" and "0to 9" then "true"
str1 = "Welcome"
print(str1.isalpha()) # alphanumaric "A" to "Z" "a" to "z"  then "true"

str1 = "hello world"
print(str1.islower())  

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization"   #all words in capital then title
print(str1.istitle())   #True

str2 = "To kill a Mocking bird"  #not all the  words in capital
print(str2.istitle())   #false

str1 = "Python is a Interpreted Language"  #Check sentence starts with Python or not
print(str1.startswith("Python"))    # True

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())  #the capital is small & small is capital 

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())