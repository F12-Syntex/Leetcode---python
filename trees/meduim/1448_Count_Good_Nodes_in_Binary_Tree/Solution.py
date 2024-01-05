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
    def goodNodes(self, root):

        #explore all paths, passing in the current max val for each exploration
        def dfs(node, maxVal):

            #if the node is none, then return 0 as an empty node cannot have any good nodes
            if not node:
                return 0
            
            #start counting the number of good nodes starting from this node
            #we start with 1 if the current node is a good node
            goodNodes = 1 if node.val >= maxVal else 0

            #computer the new max val
            maxVal = max(maxVal, node.val)

            #increment the good nodes with the good nodes of the left and right children
            goodNodes += dfs(node.left, maxVal)
            goodNodes += dfs(node.right, maxVal)

            #return the number of good nodes for this particular node
            return goodNodes
        
        #return the 
        return dfs(root, root.val)

root = TreeNode.build_tree([3,1,4,3,None,1,5])
sameTree = Solution().goodNodes(root)
print(sameTree)

