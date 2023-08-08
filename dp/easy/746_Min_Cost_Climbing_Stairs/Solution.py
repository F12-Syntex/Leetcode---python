import math

class Solution(object):
    def minCostClimbingStairs(self, cost):

        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])

        cost.append(0)
        cost.append(0)

        offset = 2
        
        length = len(cost)
        for i in range(length - offset):
            index = (length-1) - i - offset
            child1 = cost[index+1]
            child2 = cost[index+2]
            cost[index] += min(child1, child2)

        return min(cost[0], cost[1])
    

print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))