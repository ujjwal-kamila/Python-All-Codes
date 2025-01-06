# 2381. Shifting Letters II

from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)  # Convert str to list
        n = len(s)
        # Array to track shift counts
        shift_count = [0] * (n + 1)
        
        # Apply shifts to the shift_count array
        for start, end, direction in shifts:
            shift_amount = 1 if direction == 1 else -1
            shift_count[start] += shift_amount  # Increment shift at 'start'
            if end + 1 < n:
                shift_count[end + 1] -= shift_amount  # Cancel shift after 'end'
        
        # Apply cumulative shifts to the string
        total_shift = 0
        for i in range(n):
            total_shift += shift_count[i]  # Sum up shifts
            # Update character by shifting based on total shift count
            s[i] = chr(((ord(s[i]) - 97 + total_shift) % 26) + 97)
        
        # Convert list of characters back to string and return
        return ''.join(s)

# Test case
s = "abc"
shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
solution = Solution()
print(solution.shiftingLetters(s, shifts))  # Output: "ace"


'''
start: Starting index of the shift.
end: Ending index of the shift.
direction: 1 for forward shift, 0 for backward shift
'''


# '''
# For forward shift (direction == 1): The character’s ASCII value is increased by 1, wrapped around with % 26, and converted back to a character.
# For backward shift (direction == 0): The character’s ASCII value is decreased by 1, wrapped with % 26, and converted back to a character.
# also
# The number 26 ensures wrapping within the 26 letters of the alphabet when shifting.

# '''






