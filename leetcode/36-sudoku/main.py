"""
    1st: very straight forward solution
    time		O(3n)
    space 	    O(n)
    68 ms, faster than 98.24%
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(len(board)):
            hs = set()
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in hs:
                    return False
                hs.add(board[i][j])
        for j in range(len(board[0])):
            hs = set()
            for i in range(len(board)):
                if board[i][j] == '.':
                    continue
                if board[i][j] in hs:
                    return False
                hs.add(board[i][j])
        corners = [
            (0, 0), (0, 3), (0, 6),
            (3, 0), (3, 3), (3, 6),
            (6, 0), (6, 3), (6, 6),
        ]

        for i in range(len(corners)):
            b = self.checkGrid(board, corners[i][0], corners[i][1])
            if b == False:
                return False
        return True

    def checkGrid(self, board, x, y):
        hs = set()
        for i in range(x, x+3):
            for j in range(y, y+3):
                if board[i][j] == '.':
                    continue
                if board[i][j] in hs:
                    return False
                hs.add(board[i][j])
        return True


s = Solution()

a = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]

print(s.isValidSudoku(a))