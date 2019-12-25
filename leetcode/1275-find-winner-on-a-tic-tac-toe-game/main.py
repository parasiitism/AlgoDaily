from collections import defaultdict

"""
    1st: brute-force

    Time    O(1)
    Space   O(1)
    20 ms, faster than 63.77%
"""


class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        board = [['', '', ''] for _ in range(3)]
        for i in range(len(moves)):
            x, y = moves[i]
            if i % 2 == 0:
                board[x][y] = 'A'
            else:
                board[x][y] = 'B'

        # horizontal
        for i in range(len(board)):
            counts = defaultdict(int)
            for j in range(len(board[0])):
                counts[board[i][j]] += 1
            if counts['A'] == 3:
                return 'A'
            if counts['B'] == 3:
                return 'B'
        # vertical
        for j in range(len(board[0])):
            counts = defaultdict(int)
            for i in range(len(board)):
                counts[board[i][j]] += 1
            if counts['A'] == 3:
                return 'A'
            if counts['B'] == 3:
                return 'B'
        # diagonal
        countsDiag1 = defaultdict(int)
        countsDiag2 = defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == j:
                    countsDiag1[board[i][j]] += 1
                if i+j == 2:
                    countsDiag2[board[i][j]] += 1
        if countsDiag1['A'] == 3:
            return 'A'
        if countsDiag1['B'] == 3:
            return 'B'
        if countsDiag2['A'] == 3:
            return 'A'
        if countsDiag2['B'] == 3:
            return 'B'
        if len(moves) == 9:
            return 'Draw'
        return 'Pending'
