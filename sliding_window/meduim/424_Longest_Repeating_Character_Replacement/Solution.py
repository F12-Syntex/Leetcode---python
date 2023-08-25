from collections import defaultdict

class Solution(object):
    def characterReplacement(self, s, k):
        l = 0
        curr = 0
        freq = defaultdict(int)
        maxF = 0
        
        for r in range(len(s)):
            freq[s[r]] += 1
            maxF = max(maxF, freq[s[r]])
            
            if (r - l + 1) - maxF > k:
                freq[s[l]] -= 1
                l += 1
            
            curr = max(curr, r - l + 1)
        
        return curr

print(Solution().characterReplacement("ABAB", 2))
