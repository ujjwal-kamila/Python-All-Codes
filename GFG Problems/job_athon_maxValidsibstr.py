# maximum valid substr
class Solution:
    def modMatch(self, arr, y):
        # Reduce array elements to last digit only
        arr = [a % 10 for a in arr]

        # Keep at most 3 occurrences of each digit
        freq = {}
        reduced = []
        for num in arr:
            if freq.get(num, 0) < 3:
                reduced.append(num)
                freq[num] = freq.get(num, 0) + 1

        # Check all triplets
        n = len(reduced)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (reduced[i] * reduced[j] * reduced[k]) % 10 == y:
                        return True
        return False


# test cases
s = Solution()

print(s.modMatch([12, 23, 34, 45], 0))  
print(s.modMatch([1, 2, 3, 4], 4))      
print(s.modMatch([7, 17, 27], 3))      
