class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l, r = 0, 0

        res = 0

        while r < len(s):
            i = s[r]
            curr = s[l:r]

            if i in curr:
                size = r - l
                if res < size:
                    res = size

                l += curr.index(i) + 1

            r+=1
        
        return max(res, (r - l))

print(Solution().lengthOfLongestSubstring("jbpnbwwd"))