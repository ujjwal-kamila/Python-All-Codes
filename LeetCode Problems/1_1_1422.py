# 1422. Maximum Score After Splitting a String

def maxscore(self ,s) -> int:
    max_score = 0
    count_0left = 0
    count_1right = 0
    length = len(s)
    
    for i in range(length):
        if length[i]=='1':
            count_1right += 1
        
    for i in range(length-1):
        if s[i] == '0':
            count_0left += 1
        else:
            
            count_1right += 1
        
        score = count_0left + count_1right
        max_score = max(max_score, count_0left + count_1right)
    
    return max_score


s = "011101"
print(maxscore(s))