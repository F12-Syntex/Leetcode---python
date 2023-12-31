class Solution(object):

    def tribonacci(self, n):
        arr = [0, 1, 1]

        if len(arr) >= n:
            return arr[n]
        
        for i in range(3, n):
            num = arr[0] + arr[1] + arr[2]
            self.leftShift(arr)
            arr.append(num)
        
        return self.sum(arr)
    
    def sum(self, arr):
        sum = 0
        for i in arr:
            sum+=i
        return sum
        
    def leftShift(self, arr):
        for i in range(1, len(arr)):
            arr[i-1] = arr[i]
        arr.pop()

    
print(Solution().tribonacci(4))