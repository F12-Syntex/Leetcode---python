class Solution(object):
    def isSubsequence(self, string, text):
        subsequence = list(string)
        j = 0
        for i in range(len(text)):
            if(text[i] == subsequence[j]):
                char = subsequence[j]
                j+=1
                if(len(subsequence) == j):
                    return True
        return False
        


print(Solution().isSubsequence("abc", "ahbgdc"))