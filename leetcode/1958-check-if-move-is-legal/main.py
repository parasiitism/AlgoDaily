"""
    1st: brute force array
    - check all the direction from input cell

    Time    O(32)
    Space   O(1)
    40 ms, faster than 99.09%
"""


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0),
                (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for di, dj in dirs:
            i = rMove + di
            j = cMove + dj
            length = 2
            while 0 <= i < 8 and 0 <= j < 8:
                if board[i][j] == '.' or (length < 3 and board[i][j] == color):
                    break
                if board[i][j] == color:
                    return True
                i += di
                j += dj
                length += 1
        return False
