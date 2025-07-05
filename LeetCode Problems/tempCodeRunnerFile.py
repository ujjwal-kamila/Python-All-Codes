# 1394. Find Lucky Integer in an Array


from collections import Counter
class Solution:
    def findLucky(self, arr):
        count = Counter(arr)
        result = -1

        for i in range(1, 501):  
            if count[i] == i:
                if i > result:
                    result = i

        return result


# test cases
sol = Solution()
res = sol.findLucky([2,2,3,4])
print("Output is :",res)

sol = Solution()
res = sol.findLucky([1,2,2,3,3,3])
res = sol.findLucky([2,2,2,3,3])
print("Output is :",res)