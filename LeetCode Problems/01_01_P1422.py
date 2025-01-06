# 1422. Maximum Score After Splitting a String

def maxscore(s) -> int:
    max_score = 0
    count_0left = 0
    count_1right = 0
    length = len(s)

    # First pass to count the total number of '1's in the string (all in the right part)
    for i in range(length):
        if s[i] == '1':
            count_1right += 1
    
    # Second pass to calculate max score after splitting at each position
    for i in range(length - 1): 
        if s[i] == '0':
            count_0left += 1
        else:
            count_1right -= 1  # When moving the split past '1', remove it from the right part
        
        score = count_0left + count_1right
        max_score = max(max_score, score)
    
    return max_score

# Test case
s = "011101"
print(maxscore(s))  # 5
