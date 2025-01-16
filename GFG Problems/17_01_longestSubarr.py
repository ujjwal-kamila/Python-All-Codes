# Largest subarray of 0's and 1's

# Input: arr[] = [1, 0, 1, 1, 1, 0, 0]
# Output: 6
# Explanation: arr[1...6] is the longest subarray with three 0s and three 1s.

'''
Approach:
1.Convert 0 to -1 in the array.
2.Track prefix sum as you iterate. If the sum repeats, it means there's a subarray with equal 0s and 1s.
3.Use a dictionary to store the first occurrence of each prefix sum.
4.The difference between the current index and the first occurrence of a repeating prefix sum gives the length of the subarray.

'''


from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Dictionary to store the first occurrence of a prefix sum
        prefix_sum_map = {0: -1}  # Initialize with 0: -1 to handle cases starting from the first index
        max_length ,prefix_sum = 0,0
        
        
        for i in range(len(nums)):
            # Change 0 to -1 to make sum calculation easier
            prefix_sum += 1 if nums[i] == 1 else -1
            
            # If the prefix sum has been seen before, calculate the length of the subarray
            if prefix_sum in prefix_sum_map:
                # Update the max length if we find a longer subarray
                max_length = max(max_length, i - prefix_sum_map[prefix_sum])
            else:
                # Store the first occurrence of the prefix sum
                prefix_sum_map[prefix_sum] = i
        
        return max_length


# Test Cases:
nums1 = [1, 0, 1, 1, 1, 0, 0]
nums2 = [0, 0, 1, 1, 0]
nums3 = [0,0,1]

print(Solution().findMaxLength(nums1))  # Output: 6
print(Solution().findMaxLength(nums2))  # Output: 4
print(Solution().findMaxLength(nums3))  # Output: 2
