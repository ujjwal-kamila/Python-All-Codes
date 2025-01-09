# Indexes of Subarray Sum

# Input: arr[] = [1, 2, 3, 7, 5], target = 12
# Output: [2, 4]
# Explanation: The sum of elements from 2nd to 4th position is 12.

class Solution:
    def subarraySum(self, arr, target):
        low,total = 0, 0
        for high in range(len(arr)):
            total += arr[high]
            while total > target:
                total -= arr[low]
                low += 1
            if total == target:
                return [low+1, high+1]
        return [-1]
    
# Test case 

arr1 = [1, 2, 3, 7, 5]
target1 = 12
print(Solution().subarraySum(arr1, target1)) 


arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target2 = 15
print(Solution().subarraySum(arr2, target2))