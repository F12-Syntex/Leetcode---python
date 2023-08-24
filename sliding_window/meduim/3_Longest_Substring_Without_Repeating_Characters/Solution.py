class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l, r = 0, 0

        res = 0
        curr = ""

        while r < len(s):
            i = s[r]

            if i in curr:
                if len(curr) > res:
                    res = len(curr)
                curr = curr.split(i)[1] + i
            else:
                curr += i

            r+=1
        
        return max(res, len(curr))

print(Solution().lengthOfLongestSubstring("jbpnbwwd"))