import collections

class Solution(object):
    def maxSlidingWindow(self, nums, k):

        res = []
        q = collections.deque()
        l = 0

        for r in range(len(nums)):

            print(r)

            #remove all smaller values at the end of the dequeue
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            
            #add the value to the queue, which is the smallest element in the queue
            q.append(r)

            #remove the element which is now out of bounds
            #if the first element in our queue, is less than the left pointer, then it is out of bounds
            if q[0] < l:
                q.popleft()

            #add values to our output
            if (r + 1) >= k:
                #add the max, which is the left most value in our queue
                res.append(nums[q[0]])
                l+=1

        return res
    
print(Solution().maxSlidingWindow([2,4,7], 2))