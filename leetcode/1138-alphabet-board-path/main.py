"""
    1st approach: BFS + hashtable
    - similar to lc200
    - for each character in target
        - we look for the shortest path to the character from the start point
        - after we reach to the character we construct our result & update the start point
    
    Time    O(kn) k: length of target, n: board
    Space   O(n)
    40 ms, faster than 10.96%
"""


class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        startI, startJ = 0, 0
        res = ''
        for c in target:
            i, j, path = self.bfs(board, startI, startJ, c)
            startI, startJ = i, j
            res += path + '!'
        return res

    def bfs(self, board, startI, startJ, target):
        q = [(startI, startJ, '')]
        hs = set()
        while len(q) > 0:
            i, j, path = q.pop(0)
            if board[i][j] == target:
                return i, j, path
            if (i, j) in hs:
                continue
            hs.add((i, j))
            if i - 1 >= 0:
                q.append((i-1, j, path + 'U'))
            if i + 1 < len(board) and j < len(board[i+1]):
                q.append((i+1, j, path + 'D'))
            if j - 1 >= 0:
                q.append((i, j-1, path + 'L'))
            if j + 1 < len(board[i]):
                q.append((i, j+1, path + 'R'))
