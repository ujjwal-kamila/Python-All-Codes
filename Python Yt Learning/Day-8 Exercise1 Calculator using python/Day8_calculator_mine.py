# Create a calculator using python 
# Add function
def add(x, y):
    return x + y

# subtract function

def subtract(x, y):
    return x - y

# multiply function

def multiply(x, y):
    return x * y

# divide function

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y
    
# floor_divide function

def floor_divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x // y
    
# modulo function

def modulo(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x % y
    
# exponentiate function

def exponentiate(x, y):
    return x ** y

print("Welcome to the Python Calculator!")
print("Select operation(1 to 7):")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Floor Divide")
print("6. Modulo")
print("7. Exponentiate")

while True:
    choice = input("Enter choice (1/2/3/4/5/6/7): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
            
        elif choice == '2':
            print("Result:", subtract(num1, num2))
            
        elif choice == '3':
            print("Result:", multiply(num1, num2))
            
        elif choice == '4':
            print("Result:", divide(num1, num2))
            
        elif choice == '5':
            print("Result:", floor_divide(num1, num2))
        elif choice == '6':
            print("Result:", modulo(num1, num2))
            
        elif choice == '7':
            
            print("Result:", exponentiate(num1, num2))
        break
    else:
        print("Invalid Input")
