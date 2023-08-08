from TreeNode import TreeNode

class Solution(object):
    def allPossibleFBT(self, n):
        
        cache = {
            0 : [],
            1 : [TreeNode()]
        }

        def explore(n):
            if n in cache:
                return cache[n]
            
            solutions = []

            for left in range(n):
                right = n - left - 1

                leftTree = explore(left)
                rightTree = explore(right)

                for lt in leftTree:
                    for rt in rightTree:
                        solutions.append(TreeNode(0, lt, rt))

            cache[n] = solutions
            return solutions
            
        return explore(n)

result = Solution().allPossibleFBT(5)
for tree in result:
    print("-", tree)