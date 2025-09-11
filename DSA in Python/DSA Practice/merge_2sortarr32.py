# Merge two sorted arrays without any duplicates

def merge_sorted_arr(nums1,nums2):
    n = len(nums1)
    m = len(nums2)
    i = 0 
    j = 0
    res =[]     # result array
    # merge until one array ends
    while i<n and j<m:
        if nums1[i] <=nums2[j]:
            if len(res) ==0 or nums1[i]!=res[-1]:  # avoid duplicates
                res.append(nums1[i])
            i+=1
        
        else:  # when nums2 has small nums
            if len(res) ==0 or nums2[j]!=res[-1]:
                res.append(nums2[j])
            j+=1
        
        # when j exhaust
        while i<n:
            if len(res) ==0 or nums1[i]!=res[-1]:   # avoid duplicates
                res.append(nums1[i])
            i+=1
        
        # when i exhaust
        while j<m:
            if len(res) ==0 or nums2[j]!=res[-1]:
                res.append(nums2[j])
            j+=1
        return res

arr1 = [1, 2, 2, 3, 5]
arr2 = [2, 3, 4, 5, 6]
 
print("Merges array :",merge_sorted_arr(arr1, arr2))
