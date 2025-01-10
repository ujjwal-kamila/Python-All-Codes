# Count distinct array elements in every window with givem size k

# Input: arr[] = [1, 2, 1, 3, 4, 2, 3], k = 4
# Output:  [3, 4, 4, 3]
# Explanation: Window 1 of size k = 4 is 1 2 1 3. Number of distinct elements in this window are 3. 
# Window 2 of size k = 4 is 2 1 3 4. Number of distinct elements in this window are 4.
# Window 3 of size k = 4 is 1 3 4 2. Number of distinct elements in this window are 4.
# Window 4 of size k = 4 is 3 4 2 3. Number of distinct elements in this window are 3.



from collections import defaultdict

def count_distinct(arr, k):
    n = len(arr)
    if n < k:
        return []

    # Dictionary to store element frequencies
    freq = defaultdict(int) 

    # Initialize with first window
    for i in range(k):
        freq[arr[i]] += 1

    # Count distinct elements in the first window
    distinct_count = len(freq)
    result = [distinct_count]

    # Slide the window
    for i in range(k, n):
        # Remove leftmost element
        freq[arr[i - k]] -= 1
        if freq[arr[i - k]] == 0:   # if 0 then remove it from dict
            del freq[arr[i - k]] 

        # Add rightmost element
        freq[arr[i]] += 1

        # Update distinct count
        distinct_count = len(freq)
        result.append(distinct_count)

    return result

# Example usage
arr = [1, 2, 1, 3, 4, 2, 3]
k = 4
print(count_distinct(arr, k))  # Output: [3, 4, 4, 3]
