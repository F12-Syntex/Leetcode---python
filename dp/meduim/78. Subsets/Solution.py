class Solution:
    def subsets(self, nums):
        res = []
        subsets = []

        def dfs(index):
            if index >= len(nums):
                res.append(subsets.copy())
                return
            
            subsets.append(nums[index])
            dfs(index + 1)

            subsets.pop()
            dfs(index + 1)

        dfs(0)
        return res
            

        