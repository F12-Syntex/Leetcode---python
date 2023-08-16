class Solution(object):
    def search(self, nums, target):

        l, r = 0, len(nums)

        while(l < r):
            middleIndex = l + ((r - l) // 2)
            if nums[middleIndex] < target:
                if l == middleIndex:
                    return -1
                l = middleIndex
            elif nums[middleIndex] > target:
                if r == middleIndex:
                    return -1
                r = middleIndex
            else:
                return middleIndex


        return -1
    

print(Solution().search([-1,0,3,5,9,12], 2))