#  Remove Duplicates from a Sorted Array 


from typing import List

# Brute force approach 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        freq_map={}
        
        for i in range(0,n):
            freq_map[nums[i]] = 0
        
        j = 0
        for key in freq_map:
            nums[j] = key
            j+=1
        return j

# test cases
sol = Solution()
nums = [1,1,2]
res = sol.removeDuplicates(nums)
print(res)
print(nums[:res])  # count upto unique


# optimal solution 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n ==1:
            return 1
                
        i = 0
        j = i+1
        while j < n:
            if nums[j]!=nums[i]:
                i+=1
                nums[j],nums[i] = nums[i],nums[j]
            j+=1

        return i+1
    
sol = Solution()
nums = [1,1,2]
res = sol.removeDuplicates(nums)
print(res)
print(nums[:res])  # count upto unique
