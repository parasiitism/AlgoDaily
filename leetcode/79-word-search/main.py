"""
    questions to ask:
    - what if the word is an empty string? return true
    - will the board be empty? yes 
"""

"""
    1st approach: backstracking

    why backtracking works but bfs doesn't work?
    consider this test case
    m = [
        ["A", "B", "C", "E"],
        ["S", "F", "E", "S"],
        ["A", "D", "E", "E"],
    ]
    word = ABCESEEEFS

    1. If we do bfs, we marked the S,F,E on the second row as seen 
        before we are going to explore it from the bottom-right E.

    2. backtracking is actually a dfs, if a recursion exits, 
        it 'unseen' the explored coordinates such that we can explore all possibilities.

    Time    O(4^L) L: length of target word
    Space   O(M*N + L)
    364 ms, faster than 33.86%
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0 or len(board) == 0 or len(board[0]) == 0:
            return True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    if self.dfs(i, j, word, board):
                        return True
        return False

    def dfs(self, i, j, remain, board):
        if len(remain) == 0:
            return True
        if i < 0 or i+1 > len(board) or j < 0 or j+1 > len(board[0]):
            return False
        if board[i][j] != remain[0]:
            return False

        temp = board[i][j]
        board[i][j] = "#"

        trim = remain[1:]
        res = self.dfs(i-1, j, trim, board) or self.dfs(i+1, j, trim, board)\
            or self.dfs(i, j-1, trim, board) or self.dfs(i, j+1, trim, board)

        board[i][j] = temp

        return res


class Solution(object):
    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position
    def dfs(self, board, i, j, word):
        if len(word) == 0:  # all the characters are checked
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        # first character is found, check the remaining part
        tmp = board[i][j]
        # avoid visit agian
        board[i][j] = "#"
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:])\
            or self.dfs(board, i-1, j, word[1:])\
            or self.dfs(board, i, j+1, word[1:])\
            or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res


a = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
print(Solution().exist(a, "ABCCED"))
print(Solution().exist(a, "SEE"))
print(Solution().exist(a, "ABAB"))


a = [
    ["A", "B", "C", "E"],
    ["S", "F", "E", "S"],
    ["A", "D", "E", "E"],
]
print(Solution().exist(a, "ABCESEEEFS"))
