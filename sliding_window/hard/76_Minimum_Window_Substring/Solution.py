import string

class Solution(object):
    def minWindow(self, s, t):

        countS, countT = {}, {}
        minWindow = float("infinity")
        res = [-1, -1]
        l = 0

        #fill the countT map
        for i in t:
            countT[i] = countT.get(i, 0) + 1

        have, required = 0, len(countT)

        for r in range(len(s)):
            c = s[r]

            #update the frequency of the current character
            countS[c] = countS.get(c, 0) + 1

            #check if we met a condition
            if c in countT and countT[c] == countS[c]:
                have += 1

            #whlie our window is valid
            while have >= required:
                
                #update the new min
                windowSize = r - l + 1
                if windowSize < minWindow:
                    minWindow = windowSize
                    res = [l, r]

                #pop the left character
                countS[s[l]] -= 1

                #check if we no longer met a condition
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1

                #decrement the left pointer
                l+=1

        #set our new pointers based on the result
        l, r = res

        #return the min substring if it exists, else return an empty string
        return "" if minWindow == float("infinity") else s[l:r+1]

print(Solution().minWindow("ADOBECODEBANC", "ABC"))