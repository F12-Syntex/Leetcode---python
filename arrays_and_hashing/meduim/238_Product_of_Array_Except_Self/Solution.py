class Solution(object):
    def productExceptSelf(self, nums):
        answer = [0] * len(nums)

        sum = 1
        zeroIndex = -1

        for i in range(len(nums)):
            value = nums[i]
            if value == 0:
                if zeroIndex != -1:
                    return answer
                zeroIndex = i
                continue
            sum *= value

        for i in range(len(nums)):
            if zeroIndex == -1:
                answer[i] = sum // nums[i]
                continue

            if zeroIndex == i:
                answer[i] = sum
                continue

        return answer
    
print(Solution().productExceptSelf([-1,1,0,-3,3]))