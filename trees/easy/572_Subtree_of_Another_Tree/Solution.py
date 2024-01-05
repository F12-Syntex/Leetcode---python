
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
    def isSubtree(self, root, subRoot):

        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

    def isSameTree(self, root, root2):

        if not root and not root2:
            return True
        
        if not root or not root2:
            return False
        
        if root.val != root2.val:
            return False

        return self.isSameTree(root.left, root2.left) and self.isSameTree(root.right, root2.right)

root = TreeNode.build_tree([3,4,5,1,2])
subRoot = TreeNode.build_tree([4,1,2])

sameTree = Solution().isSubtree(root, subRoot)
print(sameTree)

