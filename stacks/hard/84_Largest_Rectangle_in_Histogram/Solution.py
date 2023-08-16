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
        
        # while stack:
        #     value, index = stack.pop()
        #     maxArea = max(maxArea, value * (len(heights) - index))
            
        return maxArea

print(Solution().largestRectangleArea([3,6,5,7,4,8,1,0]))

#3, 6 : 5
#3, 5, 7, 4

#2,3,4,5,0