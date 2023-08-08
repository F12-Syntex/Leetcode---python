class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.preorder(self))

    def preorder(self, node):
        if node is None:
            return "None"
        
        left = self.preorder(node.left)
        right = self.preorder(node.right)

        return f"TreeNode({node.val}, {left}, {right})"
