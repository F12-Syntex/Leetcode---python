class Solution(object):
    def twoSum(self, numbers, target):

        rPointer = len(numbers) - 1
        lPointer = 0

        while lPointer < rPointer:
            sum = numbers[lPointer] + numbers[rPointer]
            if sum == target:
                return [lPointer + 1, rPointer + 1]
            if sum < target:
                lPointer+=1
            if sum > target:
                rPointer-=1

        return []

arr = [1,2,3,4,5]
print(Solution().twoSum(arr, 5))