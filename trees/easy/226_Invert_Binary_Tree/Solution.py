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
    def invertTree(self, root):
        
        if root == None:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root

# Create the binary tree with the values [4,2,7,1,3,6,9]
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Invert the binary tree
inverted_root = Solution().invertTree(root)

# Print the inverted tree
inverted_root.pretty_print()
