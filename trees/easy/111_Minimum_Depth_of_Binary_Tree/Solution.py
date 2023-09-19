import collections

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
    def minDepth(self, root):
        if not root:
            return 0

        self.depth = float('inf')

        def dfs(node, curDepth):
            if not node:
                return
            
            if not node.left and not node.right:
                self.depth = min(self.depth, curDepth + 1)

            dfs(node.left, curDepth + 1)
            dfs(node.right, curDepth + 1)
        
        dfs(root, 0)

        return self.depth


root = TreeNode.build_tree([2,None,3,None,4,None,5,None,6])
sameTree = Solution().minDepth(root)
print(sameTree)

