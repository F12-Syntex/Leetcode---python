# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        arr = []
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                arr.append(node.val)
        
        dfs(root)
        return arr
        