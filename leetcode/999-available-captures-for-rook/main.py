"""
    1st approach: dfs variation similar to maze

    Time    O(RC+R+C)
    Space   O(1)
    20 ms, faster than 70.17%
"""


class Solution(object):

    def __init__(self):
        self.count = 0

    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    self.explore(board, i, j)
        return self.count

    def explore(self, board, x, y):
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for di, dj in dirs:
            i = x
            j = y
            while 0 <= i + di < len(board) and 0 <= j + dj < len(board[0]):
                if board[i+di][j+dj] == 'B':
                    break
                elif board[i+di][j+dj] == 'p':
                    self.count += 1
                    break
                i = i + di
                j = j + dj
