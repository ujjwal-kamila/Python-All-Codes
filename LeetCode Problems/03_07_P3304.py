# 3304. Find the K-th Character in String Game I

class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        step = 1
        while len(word) < k:
            print(f"Step {step}:")
            print(f" Current word: {word}")
            new = ""
            for c in word:
                if c == 'z':
                    new += 'a'
                else:
                    new += chr(ord(c) + 1)
            print(f"  Generated: {new}")
            word += new
            step += 1
        print(f"\nFinal word: {word}")
        print(f"k-th character (k={k}): {word[k - 1]}")
        return word[k - 1]

# test case
sol = Solution()
sol.kthCharacter(5)
