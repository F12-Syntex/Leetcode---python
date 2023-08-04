class Solution(object):
    def maxProfit(self, prices):

        left_pointer = 0
        right_pointer = 1
        max_profit = 0

        for i in range(1, len(prices)):
            value = prices[i]

            if value < prices[left_pointer]:
                left_pointer = i

            right_pointer+=1
            profit = (value - prices[left_pointer])

            if(max_profit < profit):
                max_profit = profit

        return max_profit

print(Solution().maxProfit([7,6,4,3,1]))