import heapq

class Solution(object):
    def maxSlidingWindow(self, nums, k):

        l, r = 0, (k - 1)

        maximum = [0] * (len(nums) - r)
        heap = []

        # find max in first range
        for i in range(l, r + 1):
            heapq.heappush(heap, (-nums[i], i))  # store negation of elements in the heap

        element = -heapq.heappop(heap)[0]  # negate the value again to get the maximum element
        print(element)

        print(heap)

        

        l = (r+1)

        while(l < (len(nums) - 1)):
            index = (l - r + 1)
            # print(index, len(maximum))
            # print(maximum[index], nums[l], l)
            # print()
            maximum[index] = max(maximum[index], nums[l])
            l+=1

        return maximum
    
print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))

#[1,3,-1,-3,5,3,6,7]
#[[1], [3, 1], [3, 1, -1], [3, -1, -3], [5, -1, -3], [5, 3, -3], [6, 5, 3], [7, 6, 3]]]
#3, 3, 5, 5, 6, 7
