class Solution(object):
    def findMin(self, nums):

        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            m = ( l + r ) // 2
            res = min(res, nums[m])

            if nums[l] < nums[r]:
                return min(nums[l], res)

            if(nums[m] == nums[l]):
                l += 1
            elif nums[m] > nums[l]:
                l = m + 1
                res = min(res, nums[m])
            else:
                r = m - 1

        return res