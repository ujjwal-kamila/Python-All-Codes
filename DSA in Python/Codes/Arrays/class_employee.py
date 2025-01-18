# Contains Employee Details
class Employee:
    def __init__(self, empid=None, name=None, salary=None):
        # Initialize the Employee object with empid, name, and salary
        self.empid = empid
        self.name = name
        self.salary = salary

    def setEmpid(self, empid):
        # Set the employee ID
        self.empid = empid

    def setName(self, name):
        # Set the employee name
        self.name = name

    def setSalary(self, salary):
        # Set the employee salary
        self.salary = salary

    def getEmpid(self):
        # Get the employee ID
        return self.empid

    def getName(self):
        # Get the employee name
        return self.name
    
    def getSalary(self):
        # Get the employee salary
        return self.salary

# Create two Employee objects
e1 = Employee()
e2 = Employee(1, "Rahul", 40000)

# Set values for the first Employee object
e1.setEmpid(2)
e1.setName("Ujjwal")
e1.setSalary(50000)

# Print details of the second Employee object
print(e2.getEmpid(), e2.getName(), e2.getSalary())

# Print details of the first Employee object
print(e1.getEmpid(), e1.getName(), e1.getSalary())

# Create a third Employee object with specified empid, name, and salary
e3 = Employee(3, "Aashiq", 45000)

# Print details of the third Employee object
print(e3.getEmpid(), e3.getName(), e3.getSalary())
