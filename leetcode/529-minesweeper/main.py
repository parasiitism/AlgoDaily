"""
    1st approach:
    0. calculate the numbers surrouding the bomb(s)
    1. only unveil the bomb if we click on the bomb
    2. only unveil the number if we click on the number
    3. bfs + hashtable if we click on am empty space, stop bfs if we are on 'number' cells

    Time    O(8rc + rc)
    292 ms, faster than 19.04%
"""


class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if len(board) == 0 or len(board[0]) == 0:
            return []
        # clone
        clone = []
        for i in range(len(board)):
            temp = []
            for j in range(len(board[0])):
                temp.append(board[i][j])
            clone.append(temp)

        # calculate the numbers surrounding the bombs
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'M':
                    self.incrementSurrouding(clone, i, j)

        # click actions
        x, y = click[0], click[1]
        if clone[x][y] == 'M':
            board[x][y] = 'X'
            return board
        elif isinstance(clone[x][y], int):
            board[x][y] = str(clone[x][y])
            return board

        # ready for bfs
        seen = []
        for _ in range(len(board)):
            seen.append(len(board[0]) * [False])

        # bfs
        q = []
        q.append((x, y))
        while len(q) > 0:
            i, j = q.pop(0)
            if i < 0 or i+1 > len(clone) or j < 0 or j + 1 > len(clone[0]):
                continue
            if seen[i][j]:
                continue
            seen[i][j] = True
            if clone[i][j] == 'E':
                board[i][j] = 'B'
                q.append((i-1, j-1))
                q.append((i-1, j))
                q.append((i-1, j+1))
                q.append((i, j-1))
                q.append((i, j+1))
                q.append((i+1, j-1))
                q.append((i+1, j))
                q.append((i+1, j+1))
            elif isinstance(clone[i][j], int):
                board[i][j] = str(clone[i][j])
        return board

    def incrementSurrouding(self, board, i, j):
        self.incrementCell(board, i-1, j-1)
        self.incrementCell(board, i-1, j)
        self.incrementCell(board, i-1, j+1)
        self.incrementCell(board, i, j-1)
        self.incrementCell(board, i, j+1)
        self.incrementCell(board, i+1, j-1)
        self.incrementCell(board, i+1, j)
        self.incrementCell(board, i+1, j+1)

    def incrementCell(self, board, i, j):
        if i < 0 or i+1 > len(board) or j < 0 or j+1 > len(board[0]):
            return
        if board[i][j] == 'E':
            board[i][j] = 1
        elif isinstance(board[i][j], int):
            board[i][j] += 1


a = [
    ["M", "E", "E", "E", "E"],
    ["E", "E", "M", "E", "E"],
    ["E", "E", "E", "E", "E"],
    ["E", "E", "E", "E", "E"],
]
b = [0, 0]
print(Solution().updateBoard(a, b))
b = [0, 1]
print(Solution().updateBoard(a, b))
b = [0, 2]
print(Solution().updateBoard(a, b))
b = [3, 0]
print(Solution().updateBoard(a, b))

print("-----")

"""
    2nd approach:
    0. calculate the numbers surrouding the bomb(s)
    1. only unveil the bomb if we click on the bomb
    2. only unveil the number if we click on the number
    3. dfs + hashtable if we click on am empty space, stop bfs if we are on 'number' cells

    Time    O(8rc + rc)
    312 ms, faster than 18.41%
"""


class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if len(board) == 0 or len(board[0]) == 0:
            return []
        # clone
        clone = []
        for i in range(len(board)):
            temp = []
            for j in range(len(board[0])):
                temp.append(board[i][j])
            clone.append(temp)

        # calculate the numbers surrounding the bombs
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'M':
                    self.incrementSurrouding(clone, i, j)

        # click actions
        x, y = click[0], click[1]
        if clone[x][y] == 'M':
            board[x][y] = 'X'
            return board
        elif isinstance(clone[x][y], int):
            board[x][y] = str(clone[x][y])
            return board

        # ready for dfs
        seen = []
        for _ in range(len(board)):
            seen.append(len(board[0]) * [False])

        # dfs
        stack = []
        stack.append((x, y))
        while len(stack) > 0:
            i, j = stack.pop()
            if i < 0 or i+1 > len(clone) or j < 0 or j + 1 > len(clone[0]):
                continue
            if seen[i][j]:
                continue
            seen[i][j] = True
            if clone[i][j] == 'E':
                board[i][j] = 'B'
                stack.append((i-1, j-1))
                stack.append((i-1, j))
                stack.append((i-1, j+1))
                stack.append((i, j-1))
                stack.append((i, j+1))
                stack.append((i+1, j-1))
                stack.append((i+1, j))
                stack.append((i+1, j+1))
            elif isinstance(clone[i][j], int):
                board[i][j] = str(clone[i][j])
        return board

    def incrementSurrouding(self, board, i, j):
        self.incrementCell(board, i-1, j-1)
        self.incrementCell(board, i-1, j)
        self.incrementCell(board, i-1, j+1)
        self.incrementCell(board, i, j-1)
        self.incrementCell(board, i, j+1)
        self.incrementCell(board, i+1, j-1)
        self.incrementCell(board, i+1, j)
        self.incrementCell(board, i+1, j+1)

    def incrementCell(self, board, i, j):
        if i < 0 or i+1 > len(board) or j < 0 or j+1 > len(board[0]):
            return
        if board[i][j] == 'E':
            board[i][j] = 1
        elif isinstance(board[i][j], int):
            board[i][j] += 1


a = [
    ["M", "E", "E", "E", "E"],
    ["E", "E", "M", "E", "E"],
    ["E", "E", "E", "E", "E"],
    ["E", "E", "E", "E", "E"],
]
b = [0, 0]
print(Solution().updateBoard(a, b))
b = [0, 1]
print(Solution().updateBoard(a, b))
b = [0, 2]
print(Solution().updateBoard(a, b))
b = [3, 0]
print(Solution().updateBoard(a, b))
