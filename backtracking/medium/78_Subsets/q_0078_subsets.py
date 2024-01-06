class Solution(object):
    def subsets(self, nums):
        res = []
        subsets = []

        def dfs(index):

            if index >= len(nums):
                res.append(subsets[::])
                return
            
            #include the current element
            subsets.append(nums[index])
            dfs(index + 1)

            #exclude the current element
            subsets.pop()
            dfs(index + 1)

        dfs(0)
        return res