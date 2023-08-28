class Solution(object):
    def minWindow(self, s, t):

        if t == "":
            return ""
        
        requiredWindow, currWindow = {}, {}

        for i in t:
            requiredWindow[i] = requiredWindow.get(i, 0) + 1
        
        found, required = 0, len(t)

        res, resLen = [-1, -1], float("infinity")

        l = 0
        for r in range(len(s)):
            character = s[r]
            currWindow[character] = currWindow.get(character, 0) + 1

            if character in requiredWindow and currWindow[character] == requiredWindow[character]:
                found += 1

            while found == required:
                windowSize = r - l + 1
                if windowSize < resLen:
                    resLen = windowSize
                    res = [l, r]
                leftChar = s[l]
                currWindow[leftChar] -= 1
    
                if leftChar in requiredWindow and currWindow[leftChar] < requiredWindow[leftChar]:
                    found -= 1
                
                l+=1

        return "" if resLen == float("infinity") else s[res[0]:res[1] + 1]

print(Solution().minWindow("bbaa", "aba"))