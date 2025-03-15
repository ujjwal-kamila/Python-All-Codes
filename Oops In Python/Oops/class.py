#  Student class

class Student:
    def __init__(self):  # self as arg1
        print(id(self))
        print("Called automatically when crating object")
        
        

s1= Student()
print(id(s1))

