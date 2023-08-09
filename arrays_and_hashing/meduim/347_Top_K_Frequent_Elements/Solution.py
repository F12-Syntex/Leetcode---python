class Solution(object):
    def topKFrequent(self, nums, k):

        topMap = [[] for _ in range(len(nums) + 1)]
        map = self.mapify(nums)

        for key in map:
            value = map[key]
            topMap[value].append(key)
        
        j = 0
        topK = [[] for _ in range(k)]

        for i in range(len(topMap) - 1, -1, -1):
            value = topMap[i]
            if(len(value) == 0):
                continue
            for topValue in value:
                topK[j] = topValue
                j += 1
            if len(topK) == j:
                break

        return topK

    def mapify(self, nums):
        map = {}
        for i in nums:
            if i in map:
                map[i] += 1
                continue
            map[i] = 1

        return map
    
print(Solution().topKFrequent([1], 1))