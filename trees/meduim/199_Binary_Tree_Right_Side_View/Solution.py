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
    def rightSideView(self, root):
        res = []
        queue = collections.deque()
        queue.append(root)

        level = 1
        while queue:
            length = len(queue)

            level = []
            for i in range(length):
                cur = queue.popleft()

                if not cur:
                    continue

                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
                
            if(len(level) > 0):
                res.append(level[-1])

        return res

root = TreeNode.build_tree([1,2,3,4])
sameTree = Solution().rightSideView(root)
print(sameTree)

