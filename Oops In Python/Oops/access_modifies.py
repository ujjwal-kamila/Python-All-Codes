class Student:
    def __init__(self,name,marks,studentID,StudentPass):
        self.name = name    # public
        self._marks = marks     # protected
        # id pass ...Private 
        self.__id= studentID
        self.__pass = StudentPass
        
    def get_details(self):  # access within class
        return f"ID : {self.__id} and password : {self.__pass}"
    

s1 = Student("Ujjwal", 85, "S033", "Ujjwal@033")

# Accessing public var
print(s1.name)

# Accessing protected variable (not recommended)
print(s1._marks)

# Accessing private variable (Error)
# print(s1.__id)  # Attribute Error 


# Accessing private variable using a method
print(s1.get_details()) 

# Accessing private variable using name mangling (not recommended)
print(s1._Student__id)  
print(s1._Student__pass)  