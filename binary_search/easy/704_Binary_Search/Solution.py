class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            middleIndex = l + ((r - l) // 2)
            if nums[middleIndex] == target:
                return middleIndex
            if nums[middleIndex] < target:
                l = middleIndex + 1
            else:
                r = middleIndex - 1
        return -1
    

print(Solution().search([-1,0,3,5,9,12], 2))
