class Solution(object):
    def largestRectangleArea(self, heights):
        maxArea = 0
        stack = [] #pair: (height, index)

        for i, j in enumerate(heights):
            startIndex = i
            while stack and stack[-1][0] > j:
                value, index = stack.pop()
                length = i - index
                area = value * length
                maxArea = max(maxArea, area)
                startIndex = index
            stack.append([j, startIndex])
        
        while stack:
            value, index = stack.pop()
            length = len(heights) - index
            area = value * length
            maxArea = max(maxArea, area)

        return maxArea

print(Solution().largestRectangleArea([3,6,5,7,4,8,1,0]))

#3, 6 : 5
#3, 5, 7, 4

#2,3,4,5,0