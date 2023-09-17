class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return str(self.val)
    
    def __str__(self):
        output = []
        self.pretty_print(output, 0)
        return '\n'.join(output)
    
    def pretty_print(self, output, level=0):
        prefix = '    ' * level
        output.append(f'{prefix}{self.val}')
        if self.left:
            self.left.pretty_print(output, level + 1)
        if self.right:
            self.right.pretty_print(output, level + 1)

    @staticmethod
    def build_tree(arr, index=0):
        if index >= len(arr) or arr[index] is None:
            return None

        root = TreeNode(arr[index])
        root.left = TreeNode.build_tree(arr, 2 * index + 1)
        root.right = TreeNode.build_tree(arr, 2 * index + 2)
        return root
    
class Solution(object):
    def isValidBST(self, root):

        def isValid(node, lower, upper):
            #check if the node is empty, empty nodes are balanced BST
            if not node:
                return True
            #check if the node is within the boundries it's allowed to be in
            if not (node.val > lower and node.val < upper):
                return False
            #recursively check all it's children updating the boundries as we go
            return isValid(node.left, lower, node.val) and isValid(node.right, node.val, upper)
            
        #recursively check every children updating their boundries
        return isValid(root, float('-inf'), float('inf'))

null = None
root = TreeNode.build_tree([5,4,6,null,null,3,7])
sameTree = Solution().isValidBST(root)
print(sameTree)

