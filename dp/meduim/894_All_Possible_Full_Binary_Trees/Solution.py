from TreeNode import TreeNode

class Solution(object):
    def allPossibleFBT(self, n):
        
        #remember prev calculations
        cache = {
            0 : [],
            1 : [TreeNode()]
        }

        #explore a given noumber of nodes
        def explore(n):
            #no full binary trees can be produced with an even number of nodes
            #since the root node counts as 1, we would always have an odd number of
            #nodes remaining to fill the tree, which would mean that a node with one child 
            #will exist
            if n & 1 == 0:
                return []
            
            #return the cached data, since we've computed this number before
            if n in cache:
                return cache[n]
            
            #compute all the possible solutions
            solutions = []

            #we will find all the possible nodes for left, and right
            for left in range(n):
                #find the amount of right nodes we can have for the specified left nodes
                right = n - left - 1

                #explore the left and right trees given the specified nodes
                leftTree = explore(left)
                rightTree = explore(right)

                #for every subtree in the left and right tree, create a new parent tree with the value of 0 containing the permuatation of left and right trees
                for lt in leftTree:
                    for rt in rightTree:
                        solutions.append(TreeNode(0, lt, rt))

            #cache the solution
            cache[n] = solutions

            #return the solution
            return solutions
            
        #return the permuatations of explored trees
        return explore(n)

result = Solution().allPossibleFBT(5)
for tree in result:
    print("-", tree)