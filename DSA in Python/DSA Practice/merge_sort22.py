# Merge Sort Implementation in Python

class Solution:
    def merge_arr(self,left,right):
        res =[]
        i,j =0,0
        n = len(left)
        m=len(right)
        # merge two sorted arrays
        while i<n and j<m:
            if left[i] <=right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        
        # if the right subarray is exhaust 
        if i<n:
            while i<n:
                res.append(left[i])
                i+=1
        # if the leftt subarray is exhaust 
        if j<m:
            while j<m:
                res.append(right[j])
                j+=1
        return res
    
    
    def merge_sort(self,arr):
        if len(arr)<=1:   # base case
            return arr 
        mid = len(arr)//2
        # split two sub arr
        left_arr =arr[ :mid] 
        right_arr =arr[mid : ]
        left = self.merge_sort(left_arr)
        right = self.merge_sort(right_arr)
        # merge sorted sub arr
        return self.merge_arr(left,right)
        

# test cases

ans = Solution().merge_arr([1,2,3,4],[1,2,4,5,6])
print(ans)
ans = Solution().merge_sort([3,1,2,4,1,5,2,6,4])
print(ans)
