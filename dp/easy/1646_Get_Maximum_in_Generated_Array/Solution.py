class Solution(object):
    def getMaximumGenerated(self, n):
        if n < 2:
            return n
        
        arr = [0] * (n+1)
        arr[1] = 1

        max = arr[1]

        for i in range(2, n+1):
            if(i&1 == 0):
                arr[i] = arr[i//2]
            else:
                arr[i] = arr[i//2] + arr[(i//2) + 1]

            if arr[i] > max:
                max = arr[i]

        return max


print(Solution().getMaximumGenerated(7))