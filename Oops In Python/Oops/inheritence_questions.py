# Inheritance in Python - Practice Questions

# # Question 1: Simple Inheritance
# class Animal:
#     def sound(self):
#         return 'Some sound'

# class Dog(Animal):
#     def sound(self):
#         return 'Bark'

# obj = Dog()
# print(obj.sound())
# # What will be the output of the code above?
# '''
# Ans: Bark
# Bcz method overides as same sound()
# '''


# # Question 2: Multilevel Inheritance
# class Grandparent:
#     def family_name(self):
#         return 'Smith'

# class Parent(Grandparent):
#     pass

# class Child(Parent):
#     def family_name(self):
#         return 'Johnson'

# obj = Parent()
# print(obj.family_name())
# # What will be the output of the code above?
# '''
# Ans: Smith ..
# Bcz object is instance of Parent class
# If object is instance of child class the O/p -> Johnson
# '''


# # Question 3: Multiple Inheritance
# class A:
#     def show(self):
#         return 'A'

# class B:
#     def show(self):
#         return 'B'

# class C(A, B):
#     pass

# obj = C()
# print(obj.show())
# # What will be the output of the code above?

# '''
# Ans: A ...
# Bcz object is instance of A and B class
# According to Order .. it checks for show() in first parent A before B
# if C(B,A) the ans is :   B..
# '''



# # Question 4: Hierarchical Inheritance
# class Parent:
#     def common(self):
#         return 'Parent method'

# class Child1(Parent):
#     def specific(self):
#         return 'Child1 method'

# class Child2(Parent):
#     def specific(self):
#         return 'Child2 method'

# obj1 = Child1()
# obj2 = Child2()
# print(obj1.common())
# print(obj2.specific())
# # What will be the output of the code above?

# '''
# Ans: 
# Parent method
# Child2 method
# Bcz obj1 instance child1 inherit so .common() -> Parent method
# and ob2 instace child2 itself methos .specific() -> Child2 method
# '''



# Question 5: Hybrid Inheritance
class Base:
    def message(self):
        return 'Base class message'

class A(Base):
    def message(self):
        return 'A class message'

class B(Base):
    def message(self):
        return 'B class message'

class C(A, B):
    pass

obj = C()
print(obj.message())
# What will be the output of the code above?


# # Question 6: Using super() with Inheritance
# class Parent:
#     def show(self):
#         return 'Parent method'

# class Child(Parent):
#     def show(self):
#         return super().show() + ' and Child method'

# obj = Child()
# print(obj.show())
# # What will be the output of the code above?


# # Question 7: Constructor in Multilevel Inheritance
# class Grandparent:
#     def __init__(self):
#         print('Grandparent Constructor')

# class Parent(Grandparent):
#     def __init__(self):
#         super().__init__()
#         print('Parent Constructor')

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print('Child Constructor')

# obj = Child()
# # What will be the output of the code above?



# # Question 8: Diamond Problem in Multiple Inheritance
# class A:
#     def show(self):
#         return 'A'

# class B(A):
#     def show(self):
#         return 'B'

# class C(A):
#     def show(self):
#         return 'C'

# class D(B, C):
#     pass

# obj = D()
# print(obj.show())
# # What will be the output of the code above?


# # Question 9: Method Resolution Order (MRO)
# class A:
#     def process(self):
#         return 'A'

# class B(A):
#     def process(self):
#         return 'B'

# class C(A):
#     def process(self):
#         return 'C'

# class D(B, C):
#     pass

# obj = D()
# print(obj.process())
# # What will be the output of the code above?


# # Output of MRO
# print(D.mro())


# # Question 10: Overriding and MRO
# class A:
#     def __init__(self):
#         self.value = 'A'

# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.value = 'B'

# class C(A):
#     def __init__(self):
#         super().__init__()
#         self.value = 'C'

# class D(B, C):
#     def __init__(self):
#         super().__init__()

# obj = D()
# print(obj.value)
# # What will be the output of the code above?