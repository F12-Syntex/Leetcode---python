class Solution(object):
    def findDuplicate(self, nums):

        #find collision
        s, f = 0, 0
        while s != f or s == 0:
            #s.next
            s = nums[s]

            #f.next.next
            f = nums[f] 
            f = nums[f]

        #find duplicate
        s2 = 0
        while s != s2:
            s = nums[s]
            s2 = nums[s2]

        return s
    


print(Solution().findDuplicate([1,3,4,2,2]));
        