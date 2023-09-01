class Solution(object):
    def maxSlidingWindow(self, nums, k):

        l = 0
        currentMin = float("-infinity")
        res = []
        
        res.append(max(nums[l:k]));

        #explore the other partitions
        for r in range(k, len(nums)):
            l+=1
            currentMin = max(nums[l:r+1])
            res.append(max(nums[l:r+1]))

        return res
    
print(Solution().maxSlidingWindow([2,4,7], 2))