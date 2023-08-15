class Solution(object):
    def dailyTemperatures(self, temperatures):
        result = [0] * len(temperatures) 
        stack = [] #indexes

        for index, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                poppedIndex = stack.pop()
                result[poppedIndex] = (index - poppedIndex)
            stack.append(index)

        return result
    
print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))