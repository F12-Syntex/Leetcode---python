class Solution(object):
    def maxArea(self, walls):

        l, r = 0, len(walls) - 1

        maxArea = 0

        while l < r:
            area = min(walls[l], walls[r]) * (r - l)
            maxArea = area if area > maxArea else maxArea

            if(walls[l] < walls[r]):
                l+=1
            else:
                r-=1

        return maxArea

arr = [1,1]
print(Solution().maxArea(arr))