#print a Pattern
def print_pattern(n):
    for i in range(1, n + 1):
        print(str(i) *  i)

print_pattern(5)

# '''
# def print_pattern(n):
#     for i in range(1, n + 1):
#         print(f"{i}" * i)
        
# print_pattern(5)

# '''

def print_pattern(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

print_pattern(5)
