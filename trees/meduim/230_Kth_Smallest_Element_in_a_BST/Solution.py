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
    def kthSmallest(self, root, k):

        stack = []
        cur = root
        nth = 0

        while cur or stack:

            #go as far left as possible
            while cur:
                stack.append(cur)
                cur = cur.left
            
            #process the left node
            node = stack.pop()

            #nth represents the nth smallest node
            nth += 1

            #if nth smallest node is k, which is the kth smallest node to return, simply return the node
            if nth == k:
                return node.val

            #explore the right portion of the tree
            cur = node.right



null = None
root = TreeNode.build_tree([3,1,4,None,2])
sameTree = Solution().kthSmallest(root, 3)
print(sameTree)

