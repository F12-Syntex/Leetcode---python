# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        res = [root.val]

        def dfs(node):
            if not node:
                return 0

            maxLeft = max(0, dfs(node.left))
            maxRight = max(0, dfs(node.right))

            #calculate max with split
            route = node.val + maxLeft + maxRight

            #calculate without split
            path = node.val + max(maxLeft, maxRight)

            res[0] = max(res[0], route)

            return path
        
        dfs(root)

        return res[0]
        