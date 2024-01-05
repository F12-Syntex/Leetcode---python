class Solution(object):
    def permute(self, nums):

        #store all the results
        res = []

        #base case, check if the length is one, in which case the permutations are just the node itself
        if len(nums) == 1:
            return [nums[:]]

        #go through ever element in nums, and find the permutation if we take one elements out
        for i in range(len(nums)):
            #pop the first element and find all the permutations if we ignore this number
            curr = nums.pop(0)

            #find the permutations for this sub list
            perms = self.permute(nums)

            #for every permutation in the sub list, append the current number
            for perm in perms:
                perm.append(curr)
            
            #add all the values into our res
            res.extend(perms)

            #add the number we popped back into the nums array, as we need it for the next iteration
            nums.append(curr)

        #return the answer
        return res
        