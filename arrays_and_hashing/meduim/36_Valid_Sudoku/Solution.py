class Solution(object):
    def isValidSudoku(self, board):

        for rowIndex in range(len(board)):
            row = board[rowIndex]
            for colIndex in range(len(row)):
                if not self.verify(board, rowIndex, colIndex):
                    return False
    
        return True
    
    def verify(self, board, rowIndex, colIndex):
        valid = True
        if(rowIndex == 0):
            valid = valid and self.verifyHorizontal(board, rowIndex, colIndex)
        if(colIndex == 0):
            valid = valid and self.verifyVertical(board, rowIndex, colIndex)
        if(rowIndex / 3 == 0 and colIndex / 3 == 0):
            valid = valid and self.verifyBlock(board, rowIndex, colIndex)

        return valid
        
    def has_duplicates(arr):
        checker = 0
        for char in arr:
            if char == '.':
                continue
            char_code = ord(char)
            if (checker & (1 << char_code)) > 0:
                return True
            checker |= (1 << char_code)
        return False
    
    def verifyHorizontal(self, board, rowIndex, colIndex):
        if(rowIndex > 0):
            return True
        return not self.has_duplicates(board[colIndex])

    def verifyVertical(self, board, rowIndex, colIndex):
        col = []
        if(colIndex > 0):
            return True
        
        for i in board:
            col.append(i[rowIndex])
        return not self.has_duplicates(col)
    
    def verifyBlock(self, board, rowIndex, colIndex):
        block = [''] * 9

        blockIndexRowStart = 3 * ((rowIndex % 3))
        blockIndexColStart = 3 * ((colIndex % 3))
        blockIndexRowEnd = 3 * ((rowIndex % 3) + 1)
        blockIndexColEnd = 3 * ((colIndex % 3) + 1)

        if(rowIndex / 3 != 0 or colIndex / 3 != 0):
            return True

        index = 0

        for i in range(blockIndexRowStart, blockIndexRowEnd):
            for j in range(blockIndexColStart, blockIndexColEnd):
                block[index] = board[i][j]
                index+=1

        return not self.has_duplicates(block)

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))