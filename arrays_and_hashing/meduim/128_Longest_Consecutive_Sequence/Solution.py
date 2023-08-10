class Solution(object):
    def longestConsecutive(self, nums):
        hashset, maximum = set(nums), 0
        for i in hashset:
            if i-1 not in hashset:
                sequence = 1
                while (i+sequence) in hashset:
                    sequence += 1
                maximum = max(maximum, sequence)
        return maximum


print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))