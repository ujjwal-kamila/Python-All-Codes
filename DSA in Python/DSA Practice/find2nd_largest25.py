# Find the second largest element in an array 

# better appoach 
# two pass 
class Solution:
    def find_2ndLargest(self,arr):
        n = len(arr)
        large = float("-inf")
        s_largest = float("-inf")
        # check largest first
        for i in range(0,n):
            if arr[i] > large :
                large = arr[i]
        # check 2nd largest
        for i in range(0,n):
            if arr[i] > s_largest and arr[i]!=large:
                s_largest = arr[i]
        
        return s_largest

# test cases
ans = Solution().find_2ndLargest([1,-1,-5,6])
print(ans)
ans = Solution().find_2ndLargest([-1,-10,0,-11])
print(ans)


# optimal solution
class Solution:
    def find_2ndLargest(self,arr):
        n = len(arr)
        large = float("-inf")
        s_largest = float("-inf")

        for i in range(0,n):
            if arr[i] > large :
                s_largest = large
                large = arr[i]
                
            elif arr[i] > s_largest and arr[i]!=large:
                s_largest = arr[i]        

        return s_largest

# test cases
ans = Solution().find_2ndLargest([1,2,3,6])
print(ans)
ans = Solution().find_2ndLargest([1,10,0,11])
print(ans)





# # Brute force approach
# def find(arr):
#     arr.sort()
#     # return len(arr)-2
#     return arr[-2]

# arr= [-1,4,1,0]  
# print(find(arr))