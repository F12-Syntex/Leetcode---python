# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root: TreeNode):
        difference = abs(self.length(root.left) - self.length(root.right))
        return difference <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def length(self, root: TreeNode):
        if(root is None):
            return 0
        return 1 + max(self.length(root.left), self.length(root.right))


right = TreeNode(9)
left2 = TreeNode(3, TreeNode(4), TreeNode(4))

left = TreeNode(2, left2, TreeNode(3))

tree = TreeNode(1, left, right)

solution = Solution()  # Create an instance of the Solution class
balanced = solution.isBalanced(tree)  # Call the isBalanced method on the instance

print(balanced)

