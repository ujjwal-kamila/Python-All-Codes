#Day-52 Lambda functions in Python

# def double(x):
#     return x*2
# print(double(5))

#double using lambda without checking indentation
#use lambda func when having one line
#fun to fun pass using lambda fun

def apply(fx,value):
    return 6 + fx(value)

double = lambda x : x*2
# cube = lambda x : x**3
cube = lambda x : x*x*x
avg = lambda x,y : (x+y) / 2
avg3 = lambda a,b,c : (a+b+c)/ 3
print(double(5))
print(cube(5))
print(avg(3,7))
print(avg3(3,5,9))

#we can use "lambda x : x*x*x" instead of cube
print(apply(cube,4))  #prints 64+6 = 70
print(apply(double,5))
