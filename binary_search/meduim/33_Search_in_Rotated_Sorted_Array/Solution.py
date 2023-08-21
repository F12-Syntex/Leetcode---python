class Solution(object):
    def search(self, nums, target):

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            #left sorted portion
            elif nums[m] >= nums[l]:
                if target > nums[m]:
                    l = m + 1
                elif target < nums[l]:
                    r = m - 1
                else:
                    return m



        return -1

print(Solution().search([2,3,4,5,1], 1))