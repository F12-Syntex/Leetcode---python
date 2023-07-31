class Solution(object):
    def generate(self, numRows):
        dp = []
        for i in range(1, numRows + 1):
            array = []
            for x in range(1, i+1):
                if(x == 1 or x == i):
                    array.append(1)
                    continue
                parent = dp[i - 2]
                array.append(parent[x-2]+parent[x-1])
            dp.append(array)

        return dp
    
sol = Solution()
print(sol.generate(3))