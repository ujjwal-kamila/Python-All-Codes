# Object-Oriented Programming (OOPs) in Python


# passing args
def greet(arg1, message, recipient, tone):
    print(arg1)  # Prints the argument
    title = "OOP in Python"
    print(title) 
    print("Hello, welcome to Object-Oriented Programming!")
    
    
# list sorting
list1 = [3, 1, 2]
list1.sort()  

# Call the greet function with different arguments
greet(list1, "Good Morning", "Students", "Polite") 
string1 = "Alex"
greet(string1, "Hello", "Teacher", "Friendly") 

# class to convert Temp C to F using static and class methods
class Temperature:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit 
    # Instance method
    def get_fahrenheit(self):  
        return self.fahrenheit

    @classmethod
    def from_celsius(cls, celsius): 
        return cls(celsius * 9 / 5 + 32)

    @staticmethod
    def to_celsius(fahrenheit): 
        return (fahrenheit - 32) * 5 / 9

# Static method usage
print(Temperature.to_celsius(100))  

# Class method usage
temp = Temperature.from_celsius(0)
print(temp.get_fahrenheit())  

# Instance method usage
temp2 = Temperature(98)
print(temp2.get_fahrenheit()) 
