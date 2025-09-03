#  Right Rotate an Array by One Place

# using slicing
nums = [5, 2, 4, 8, 7, 9, 3]
n = len(nums)
print("Before:", nums)


rotate_nums = [nums[-1]] + nums[0:n-1]

print("After :",rotate_nums)


# another method 
class Solution: 
    def rightRotateByOne(self, nums):
        # in-place rotation
        last = nums.pop()      # remove last
        nums.insert(0, last)   # insert at beginning
        return nums


# test case
sol = Solution()

# Test 1
nums = [5, 2, 4, 8, 7, 9, 3]
print("Before:", nums)
print("After :", sol.rightRotateByOne(nums))

# another optimal approach
class Solution:
    def rightRotateByOne(self, nums):
        n = len(nums)
        temp = nums[n-1]
        for i in range(n-2,-1,-1):
            nums[i+1] = nums[i]
        nums[0]=temp
        
nums = [1,3,5,7,9,0]
print("Before:", nums)
print("After :", sol.rightRotateByOne(nums))
