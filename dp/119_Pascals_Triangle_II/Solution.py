class Solution(object):
    def getRow(self, rowIndex):
        arr = [0] * (rowIndex+1)

        for row in range(rowIndex + 2):
            startIndex = 0
            endIndex = row-1

            original = list(arr)
            original[startIndex] = 1
            original[endIndex] = 1

            for col in range(row):
                if(col == startIndex or col == endIndex):
                    continue
                original[col] = arr[col-1] + arr[col]
            arr = original

        return arr

print(Solution().getRow(4))