class Solution(object):
    def searchMatrix(self, matrix, target):

        m = len(matrix)
        n = len(matrix[0])

        l, r = 0, (m * n) - 1

        while l <= r:
            m = (l + r) // 2
            arrayIndex = m // n
            cellIndex = m - (arrayIndex * n)

            print(m)

            if matrix[arrayIndex][cellIndex] == target:
                return True
            elif matrix[arrayIndex][cellIndex] < target:
                l = m + 1
            else:
                r = m - 1

        return False
    

print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))