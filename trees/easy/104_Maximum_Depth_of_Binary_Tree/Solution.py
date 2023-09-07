class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return str(self.val)
    
    def pretty_print(self, level=0):
        prefix = '    ' * level
        print(prefix, self.val)
        if self.left:
            self.left.pretty_print(level + 1)
        if self.right:
            self.right.pretty_print(level + 1)

class Solution(object):
    def maxDepth(self, root):
        return 0 if not root else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Create the binary tree with the values [4,2,7,1,3,6,9]
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Invert the binary tree
maxDepth = Solution().maxDepth(root)
print(maxDepth)

