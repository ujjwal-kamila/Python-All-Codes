# Create a Python ComplexNumber class with addition, subtraction, multiplication, division, and comparison operators. 2 + 3i

class ComplexNumber:
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag

    # Magic method for display
    def __str__(self):
        if self.real == 0:
            return f"0+{self.imag}i" if self.imag != 0 else "0"  # Fix for zero real part
        elif self.imag < 0:
            return f"{self.real}{self.imag}i"
        else:
            return f"{self.real}+{self.imag}i"

    # Method to return the conjugate of the complex number
    def conjugate(self):
        return ComplexNumber(self.real, -1*self.imag)    

        
    # add method
    def __add__(self,other):
        resReal= 0
        resImag = 0
        resReal = self.real + other.real
        resImag = self.imag + other.imag
        ans = ComplexNumber(resReal,resImag)
        return ans
    
    #  Sub mehtod
    def __sub__(self,other):
        resReal= 0
        resImag = 0
        resReal = self.real - other.real
        resImag = self.imag - other.imag
        ans = ComplexNumber(resReal,resImag)
        return ans
    
    
    def __mul__(self,other):
        resReal= 0
        resImag = 0
        resReal = self.real * other.real - self.imag * other.imag
        resImag = self.real * other.imag + other.real * self.imag
        ans = ComplexNumber(resReal,resImag)
        return ans
    
    def __truediv__(self,other):
        resReal= 0
        resImag = 0
        denom = other.real**2 + other.imag**2

        ans = self * ComplexNumber(other.real/denom , (-1*other.imag)/denom)
        return ans
    
    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag
    
    def __ne__(self,other):
        return self.real != other.real and self.imag != other.imag
        
    


# Test cases
cn1 = ComplexNumber(3, 5)
print("1st Complex num :",cn1)  
cn2 = ComplexNumber(4, 8)
print("2nd Complex num :",cn2)  

# Conjugate test
cn3 = cn1.conjugate()
print("{cn1} after congucate : ",cn3) 

print("Addition Result:",cn1+cn2)
print("Substraction Result:",cn1-cn2)
print("Multiplication Result:",cn1*cn2)     # (3+5i) * (4+8i) = (3×4 - 5×8) + (3×8 + 5×4)i

print("Division Result:",cn1/cn2)
print("Equality check  : ",cn1==cn2)
print("Not Equality check : ",cn1!=cn2)




# Test Case 1:

complex1 = ComplexNumber(3, 4)
complex2 = ComplexNumber(1, -2)
assert str(complex1) == "3+4i"
assert str(complex2) == "1-2i"
assert str(complex1 + complex2) == "4+2i"
assert str(complex1 - complex2) == "2+6i"
assert str(complex1 * complex2) == "11-2i"
assert str(complex1 / complex2) == "-1.0+2.0i"
assert complex1 != complex2
print("All test cases are passed✅✅ ")



