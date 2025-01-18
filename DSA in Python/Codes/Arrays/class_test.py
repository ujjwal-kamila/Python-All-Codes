#  Test with Class
class Test:
    def __init__(self):
        self.a = 2
        self.b = 4
    # From a fun "To make instance method of this class"
    def fun():
        pass # put at least one argument "self"
    # From a fun "To make static method" use @staticmethod
    @staticmethod
    def fun2():
        pass
    # From a fun "To make class method" use @classmethod
    @classmethod
    def fun3(args): # give at least one args
        pass
    def show(self):
        print("a is :", self.a,"\n b is :", self.b)
        
        
t1 = Test()
t2 = Test()
print(t1.a ,t1.b)
print(t2.a ,t2.b)
t1.show()

# To do by user input

class Test1:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
t1 = Test1(4,5)
t2 = Test1(7,8)
print(t1.a,t1.b)
print(t2.a,t2.b)

