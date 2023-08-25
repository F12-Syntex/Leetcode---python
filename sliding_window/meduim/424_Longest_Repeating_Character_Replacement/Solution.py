class Solution(object):
    def characterReplacement(self, s, k):

        l = 0
        freq = {}
        curr = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            
            while (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l+=1

            curr = max(curr, (r - l) + 1)

        return curr

print(Solution().characterReplacement("ABAB", 2))