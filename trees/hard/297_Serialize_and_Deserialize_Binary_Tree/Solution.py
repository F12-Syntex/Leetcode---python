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
    def serialize(self, root):

        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ",".join(res)
        

    def deserialize(self, data):
        vals = data.split(",")
        self.index = 0

        def dfs():
            if vals[self.index] == "N":
                self.index += 1
                return None
            node = TreeNode(int(vals[self.index]))
            self.index += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        root = dfs()
        return root

null = None
root = TreeNode.build_tree([1, 2, 3, 4, 5])
sameTree = Solution().serialize(root)
deserializedTree = Solution().deserialize(sameTree)
print(deserializedTree)
print(root)

