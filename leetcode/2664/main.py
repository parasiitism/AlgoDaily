"""
    backtracking

    Time    O((R*C)!)
    Space   O(RC)
"""


class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        board = []
        for _ in range(m):
            board.append(n * [-1])

        def dfs(i, j, steps):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if board[i][j] != -1:
                return False
            board[i][j] = steps
            if steps == m*n-1:
                return True
            dirs = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                    (1, -2), (1, 2), (2, -1), (2, 1)]
            for di, dj in dirs:
                if dfs(i+di, j+dj, steps+1):
                    return True
            board[i][j] = -1
            return False

        b = dfs(r, c, 0)
        return board
