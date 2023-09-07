from typing import Optional

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

class Solution2(object):
    def isBalanced(self, root):
        if not root:
            return True

        l = self.height(root.left)
        r = self.height(root.right)
        d = abs(l - r)

        return d <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
    
class Solution(object):
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def explore(root):
            if not root:
                return [True, 0]
            
            l = explore(root.left)
            r = explore(root.right)

            return [(l[0] and r[0] and (abs(l[1] - r[1]) <= 1)), 1 + max(l[1], r[1])] 

        return explore(root)[0]


# Create the tree nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.right.right.right = TreeNode(4)

# Invert the binary tree
tree = Solution().isBalanced(root)

print(tree)
