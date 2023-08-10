class Solution(object):
    def threeSum(self, nums):

        sums = []

        numbers = list(nums)

        numbers.sort()

        for index, number in enumerate(numbers):

            if index > 0 and number == numbers[index - 1]:
                continue

            l, r = index + 1, len(numbers) - 1

            while l < r:
                sum = number + numbers[l] + numbers[r]
                if sum < 0:
                    l+=1
                if sum > 0:
                    r-=1
                if sum == 0:
                    sums.append([number, numbers[l], numbers[r]])
                    l +=1
                    while numbers[l] == numbers[l-1]:
                        l+=1

        return sums

arr = [-1,0,1,2,-1,-4]
print(Solution().threeSum(arr))