import string
class Solution(object):
   def checkInclusion(self, s1, s2):
        
        freqS1 = {i: 0 for i in string.ascii_lowercase}
        freqS2 = {i: 0 for i in string.ascii_lowercase}

        for i in s1:
            freqS1[i] += 1

        l = 0
        for r in range(len(s2)):
            freqS2[s2[r]] += 1

            if (r - l + 1) > len(s1):
                freqS2[s2[l]] -= 1
                l+=1


            matched = True
            for i in string.ascii_letters:
                if freqS1[i] != freqS2[i]:
                    matched = False
                    break

        return False
    
print(Solution().checkInclusion("ba", "eidbaoo"))