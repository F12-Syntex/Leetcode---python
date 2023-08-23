class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        size = len(nums1) + len(nums2)
        half = size // 2



        #if nums2 is empty
        if len(nums2) == 0:
            size = len(nums1) - 1
            if (size+1) % 2:
                return nums1[size // 2] / 1
            else:
                return (nums1[size // 2] + nums1[(size // 2) + 1]) / 2
            
        #if nums1 is empty
        if len(nums1) == 0:
            size = len(nums2) - 1
            if (size+1) % 2:
                return nums2[size // 2] / 1
            else:
                return (nums2[size // 2] + nums2[(size // 2) + 1]) / 2
            
        #run binary search on the smaller array
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        #keep looping till median is found
        l, r = 0, len(nums1)

        #nums1 is the left partition
        #nums2 is the right partition

        while True:
            m = (l + r) // 2 #index for the left partition
            j = half - m - 2 #index for the right partition, we substract 2 in order to account of indexes starting at 0, 1 for m and 1 for j

            ALeft = nums1[m] if m >= 0 else float("-infinity")
            ARight = nums1[m + 1] if (m + 1) < len(nums1) else float("infinity")

            BLeft = nums2[j] if j >= 0 else float("-infinity")
            BRight = nums2[j + 1] if (j + 1) < len(nums2) else float("infinity")

            if BLeft <= ARight and ALeft <= BRight:
                if size % 2: #odd
                    return min(ARight, BRight) / 1
                return (max(ALeft, BLeft) + min(ARight, BRight)) / 2 #even
            elif BRight < ALeft:
                r = m - 1   
            else:
                l = m + 1  
    

print(Solution().findMedianSortedArrays([2,3], [1]))