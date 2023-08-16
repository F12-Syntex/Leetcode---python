class Solution(object):
    def largestRectangleArea(self, heights):
        maxArea, stack = 0, []
        heights.append(0)
        for i, j in enumerate(heights):
            startIndex = i
            while stack and stack[-1][0] > j:
                value, index = stack.pop()
                maxArea = max(maxArea, value * (i - index))
                startIndex = index
            stack.append([j, startIndex])
        return maxArea

print(Solution().largestRectangleArea([3,6,5,7,4,8,1,0]))