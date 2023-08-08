class Solution(object):
    def divisorGame(self, n):
        return n&1 == 0
    

print(str(Solution().divisorGame(3)))