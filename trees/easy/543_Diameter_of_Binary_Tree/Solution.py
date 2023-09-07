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

    def __init__(self) -> None:
        self.res = 0

    def diameterOfBinaryTree(self, root):      

        res = 0

        def dfs(root):
            if not root:
                return -1
            
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)

            diameter = leftHeight + rightHeight + 2

            self.res = max(self.res, diameter)

            return 1 + max(leftHeight, rightHeight)

        dfs(root)

        return self.res
    

# Create the binary tree with the values [1,2,3,4,5]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Invert the binary tree
res = Solution().diameterOfBinaryTree(root)

print(res)
