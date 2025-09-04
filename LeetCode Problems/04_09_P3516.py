# 3516. Find Closest Person


'''
x is the position of Person 1.
y is the position of Person 2.
z is the position of Person 3, who does not move.
'''

'''
return 1 -> if person 1 reach first
return 2 -> if person 2 reach first
return 0 -> if both reach same'''

# find absolute distance val and return using loop 


class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        d1=abs(x-z)
        d2 =abs(y-z)
        # print(d1)
        # print(d2)

        if d1 < d2:
            return 1
        elif d2 < d1:
            return 2
        else:
            return 0

sol = Solution()
res = sol.findClosest(2,7,4)
print(res)
print()
res = sol.findClosest(2,5,6)
print(res)