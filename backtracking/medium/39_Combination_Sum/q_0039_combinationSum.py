class Solution(object):
    def combinationSum(self, arr, target):
        res = []
        combinations = []
        
        def dfs(index, current_sum):
            #base case to check if our combinations sum up to the target
            if current_sum == target:
                res.append(combinations[::])
                return 

            #base cases, making sure that we don't go over the target sum and that our pointer is within the array
            if current_sum > target:
                return
            if index >= len(arr):
                return

            #include the current value in our subtree
            combinations.append(arr[index])
            dfs(index, current_sum + arr[index])

            #don't include the current value in our subtree
            combinations.pop()
            dfs(index + 1, current_sum)

        dfs(0, 0)
        return res
        