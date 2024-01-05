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
    def build_tree(arr, index):
        if index >= len(arr) or arr[index] is None:
            return None

        root = TreeNode(arr[index])
        root.left = TreeNode.build_tree(arr, 2 * index + 1)
        root.right = TreeNode.build_tree(arr, 2 * index + 2)
        return root
    

class Solution(object):
    def isSameTree(self, p, q):

        if not p and not q:
            return True
        
        if not p or not q or (p.val != q.val):
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

p = [1,2,3,4]
q = [1,2,3]

# Create TreeNode variables
p_tree = TreeNode.build_tree(p, 0)
q_tree = TreeNode.build_tree(q, 0)

# Invert the binary tree
sameTree = Solution().isSameTree(p_tree, q_tree)
print(sameTree)

