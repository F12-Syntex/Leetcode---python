class Solution(object):
    def permute(self, nums):

        res = []

        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            cur = nums.pop(0)

            permutations = self.permute(nums)

            for i in permutations:
                i.append(cur)
                res.append(i)

            nums.append(cur)

        return res