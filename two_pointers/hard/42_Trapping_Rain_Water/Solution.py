class Solution(object):
    def trap(self, height):

        length = len(height)

        l, r, level = 0, length - 1, 0
        maxL, maxR = height[l], height[r]

        while l < r:

            waterLevel = 0

            if maxL < maxR:
                l += 1
                waterLevel = maxL - height[l]
                maxL = maxL if maxL > height[l] else height[l]
            else:
                r -= 1
                waterLevel = maxR - height[r]
                maxR = maxR if maxR > height[r] else height[r]

            if waterLevel > 0:
                level += waterLevel

        return level

arr = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(arr))