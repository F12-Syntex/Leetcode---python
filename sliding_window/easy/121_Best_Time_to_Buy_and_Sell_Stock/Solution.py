class Solution(object):
    def maxProfit(self, prices):

        l, r = 0, 1
        profit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r
            r+=1

        return profit
    
print(Solution().maxProfit([7,6,4,3,1]))