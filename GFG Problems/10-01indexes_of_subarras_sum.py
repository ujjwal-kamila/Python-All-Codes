# Indexes of Subarray Sum

# Input: arr[] = [1, 2, 3, 7, 5], target = 12
# Output: [2, 4]
# Explanation: The sum of elements from 2nd to 4th position is 12.

class Solution:
    def subarraySum(self, arr, target):
        low, total = 0, 0
        for high in range(len(arr)):  # Iterate through the array
            total += arr[high]  # Add the current element to the total sum
            while total > target:  # Shrink the window from the left if sum exceeds target
                total -= arr[low]
                low += 1  # Move the left pointer to the right
            if total == target:  # Check if the current sum matches the target
                return [low + 1, high + 1]  # Return the 1-based indices of the subarray
        return [-1]  # Return [-1] if no subarray matches the target sum

    
# Test case 

arr1 = [1, 2, 3, 7, 5]
target1 = 12
print(Solution().subarraySum(arr1, target1)) 


arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target2 = 15
print(Solution().subarraySum(arr2, target2))