class Solution(object):
    def minimumDifference(self, nums, k):
        arr = sorted(nums)
        l, r = 0, k - 1
        diff = arr[len(arr) - 1] - arr[0]

        while r < len(arr):
            cur = arr[r] - arr[l]
            print(cur)
            diff = min(diff, cur)
            r+=1
            l+=1

        return diff

print(Solution().minimumDifference([9,4,1,7], 2))
        