#  Create a Student class with name ,age ,roll,branch
# methods play study 

class Student:
    def __init__(self,name,age,roll,branch):  # self as arg1
        # print("Called automatically when crating object")
        self.name = name 
        self.age = age
        self.roll = roll
        self.branch = branch
    
    #  methods
    def study(self):
        print(f"{self.name} is studying ")
    
    def play(self):
        print(f"{self.name} is playing ")
    
    def greeting(self):
        print(f"Hello :) My name is {self.name} ")
    
    def display_details(self):
        return (f"Student Name: {self.name}\n"
                f"Student Age: {self.age}\n"
                f"Student Roll: {self.roll}\n"
                f"Student Branch: {self.branch}\n")

s1 = Student("Ujjwal Kamila",20,33,'CSE')
s2 = Student("Aashiq",22,48,'CSE')


# display Details of Students 
print("Student 1 Details :\n")
print(s1.display_details())

print("Student 2 Details :\n")
print(s2.display_details())


#  Calling Methods 
s1.study()
s1.play()
s1.greeting()

s2.study()
s2.play()
s2.greeting()
