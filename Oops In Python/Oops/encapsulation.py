# Encapsulation : data and methods hide in a single class as Ex: 
# Creating a Student Class 
class Student:
    __totalStudents = 0  
    __schoolName = "XYZ High School"

    # Constructor (__init__) - used to initialize object attributes
    def __init__(self, name, rollNumber, marks):
        """
        Constructor to initialize student attributes.
        'self' refers to the current instance of the class.
        """
        self.name = name  
        self.rollNumber = rollNumber  
        self.__marks = marks
        Student.__totalStudents += 1
        
    def getMarks(self):
        return self.__marks
    
    
    # Security check 
    def setMarks(self,newMarks,passCode):
        if (passCode == self.__auth()):
            self.__marks= newMarks
        else:
            return "Wrong Passcode"
        
    
    @staticmethod       
    def getSchoolName():
        return Student.__schoolName
        
    @staticmethod
    def setSchoolName(newSchoolName,passCode):
        Student.__SendMail()
        Student.__schoolName = newSchoolName

    @staticmethod
    def __SendMail():
        print("Sending the mail to all members")

    def getStudentSchoolName(self):
        return Student.__schoolName 
    
    @staticmethod
    def getTotalStudents():
        return Student.__totalStudents   
    
    
    
    def __auth(self):
        return "0000"


    # Instance Methods
    def study(self):
        print(f"I am {self.name} with roll number {self.rollNumber}, and I am studying.")

    def play(self):
        print(f"{self.name} finished studying, now going to play.")
        
        

# Creating student objects
student1 = Student("Raj", 1, 85)  # Object 
student2 = Student("David", 2, 92)  # Another object
student3 = Student("Rahul", 3, 78)  # Another object


# Accessing a class variable using dot(.) 
print("School Name:", Student.getSchoolName())

# total number of students
print("\nTotal Students:", Student.getTotalStudents())

# Calling instance methods
student1.study()  
student2.play() 


# # Checking memory locations ids of objects
# print("Memory Address of student1:", id(student1))
# print("Memory Address of student2:", id(student2))
# print(id(student1)==id(student2))   # diff object 

# student1.setMarks(99,"0000")
# print(Student._Student__SendMail())   # break encapsulation 
# not recomnended mangeling 
# # Accessing private variable using name mangling
# print(student1._Student__marks)



Student.setSchoolName("MHS","000")



# Static Method Inside a Class
class Temperature:
    @staticmethod
    def to_celsius(fahrenheit): # No `self`
        return (fahrenheit - 32) * 5 / 9

print(Temperature.to_celsius(98))  # Output: 36.66
