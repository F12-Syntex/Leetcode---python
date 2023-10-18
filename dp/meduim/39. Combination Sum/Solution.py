class Solution:
    def combinationSum(self, candidates, target):
        res = []
        permutation = []

        def dfs(index):
            if index >= len(candidates) or sum(permutation) >= target:
                if(sum(permutation) == target):
                    res.append(permutation.copy())
                return
            
            permutation.append(candidates[index])
            dfs(index + 1)
            dfs(index)

            permutation.pop()
            dfs(index + 1)
        
        dfs(0)

        ans = []

        for i in res:
            if i not in ans:
                ans.append(i)
        
        return ans
        