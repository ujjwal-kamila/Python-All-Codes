# Recursion theory : fun called itself
# head recursion: first job then fun call
# sample fun to print name 4 times
count = 0
def print_name(name):
    global count
    if count == 4:
        return 
    print(name)
    count += 1
    print_name(name)

print_name("ujjwal")
print()


# tail recursion : first fun call then job(also called backtracking)
# using tail recursion
# print name n times
count = 0
def print_name(name):
    global count
    if count == 4:
        return 
    count += 1
    print_name(name)
    print(name)

print_name("ujjwal")