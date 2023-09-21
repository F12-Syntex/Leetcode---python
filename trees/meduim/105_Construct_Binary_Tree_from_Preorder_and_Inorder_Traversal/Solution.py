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
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        #the first value in the preorder array is always going to be the head of the tree
        root = TreeNode(preorder[0])
        
        #find the index of the root in the in order array, we do this because all values to the left of the root
        #will be in the left subtree, and all values in the right of root will be in the right subtree
        #that's how inorder traversal works, left < node > right
        mid = inorder.index(preorder[0])

        #set the left child to by building the tree, where the preorder is the value after the root till the mid
        #the reason it's partitioned till the mid is because anything past the mid value is going to be reserved for the right subtree
        #we pass in in order with values from 0 to mid, because anything after mid is for the right subtree
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])

        #set the right chlid by building the tree, where the preorder value is everything after the mid point, since everything before 
        #the mid point ( which is the index of the parent ) is reserced for the left sub tree
        #we apply the same logic for the inorder
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root

null = None
sameTree = Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])
print(sameTree)

