# Object-Oriented Programming (OOPs) in Python


# passing args
def greet(arg1, message, recipient, tone):
    """Function to print a greeting message."""
    print(arg1)  # Prints the argument
    title = "OOP in Python"
    print(title) 
    print("Hello, welcome to Object-Oriented Programming!")
    
    
# list sorting
list1 = [3, 1, 2]
list1.sort()  

# Call the greet function with different arguments
greet(list1, "Good Morning", "Students", "Polite")  # Example function call
string1 = "Alex"
greet(string1, "Hello", "Teacher", "Friendly")  # Example function call

# Creating a Student Class
class Student:
    """Student class to store details about students."""

    totalStudents = 0  
    schoolName = "XYZ High School"

    # Constructor (__init__) - used to initialize object attributes
    def __init__(self, name, rollNumber, marks):
        """
        Constructor to initialize student attributes.
        'self' refers to the current instance of the class.
        """
        self.name = name  
        self.rollNumber = rollNumber  
        self.marks = marks  
        Student.totalStudents += 1

    # Instance Methods
    def study(self):
        print(f"I am {self.name} with roll number {self.rollNumber}, and I am studying.")

    def play(self):
        print(f"{self.name} finished studying, now going to play.")

# Creating student objects
student1 = Student("Raj", 1, 85)  # Object 
student2 = Student("David", 2, 92)  # Another object

# Accessing a class variable using dot(.) 
print("School Name:", Student.schoolName)

# total number of students
print("Total Students:", Student.totalStudents)

# Calling instance methods
student1.study()  
student2.play() 

# Checking memory locations ids of objects
print("Memory Address of student1:", id(student1))
print("Memory Address of student2:", id(student2))
print(id(student1)==id(student2))   # diff object 
