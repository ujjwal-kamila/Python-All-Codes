# Check if an Array is Sorted

# brute force 
class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        return arr == sorted(arr)

# optimal approach
class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        n = len(arr)
        for i in range(n - 1):           
            if arr[i] > arr[i + 1]:     
                return False
        return True
    
    
# test cases
sol = Solution()

print(sol.arraySortedOrNot([1, 2, 3, 4, 5]))   
print(sol.arraySortedOrNot([1, 2, 2, 3, 3, 4])) 
