import math

class Solution(object):
    def minEatingSpeed(self, piles, h):

        l, r = 1, max(piles)
        minimum = r

        while l <= r:
            k = (l + r) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                minimum = min(minimum, k)
                r = k-1
            else:
                l = k+1

        return minimum
    
print(Solution().minEatingSpeed([3,6,7,11], 8))