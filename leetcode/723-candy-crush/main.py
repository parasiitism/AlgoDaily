"""
    1st: linked list
    - find the target cells from the rows and cols
    - use linked lists to build the new board

    Time    k * O(RC * (R+C) + 2RC) worst case of k = 50/3
    Space   O(RC)                   the linekd list + new board
    296 ms, faster than 10.21%
"""


class Node:
    def __init__(self, val=-1):
        self.val = val
        self.next = None


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        R, C = len(board), len(board[0])
        clone = board
        while True:
            toCollapse = set()
            for i in range(R):
                for j in range(C):
                    if clone[i][j] == 0:
                        continue
                    if i-2 >= 0 and clone[i][j] == clone[i-1][j] == clone[i-2][j]:
                        toCollapse.add((i, j))
                        toCollapse.add((i-1, j))
                        toCollapse.add((i-2, j))
                    if j-2 >= 0 and clone[i][j] == clone[i][j-1] == clone[i][j-2]:
                        toCollapse.add((i, j))
                        toCollapse.add((i, j-1))
                        toCollapse.add((i, j-2))
            if len(toCollapse) == 0:
                break
            clone = self.buildBoard(clone, toCollapse)
        return clone

    def buildBoard(self, board, toCollapse):
        # build an array of linked lists from the bottom for every column
        R, C = len(board), len(board[0])
        linkedLists = []
        for j in range(C):
            dumphead = Node()
            cur = dumphead
            for i in range(R-1, -1, -1):
                if (i, j) in toCollapse:
                    continue
                cur.next = Node(board[i][j])
                cur = cur.next
            linkedLists.append(dumphead.next)
        # reassgin the values to a new board
        clone = [C * [0] for _ in range(R)]
        for j in range(C):
            head = linkedLists[j]
            cur = head
            i = R-1
            while cur != None:
                clone[i][j] = cur.val
                i -= 1
                cur = cur.next
        return clone


s = Solution()

a = [
    [110, 5, 112, 113, 114],
    [210, 211, 5, 213, 214],
    [310, 311, 3, 313, 314],
    [410, 411, 412, 5, 414],
    [5, 1, 512, 3, 3],
    [610, 4, 1, 613, 614],
    [710, 1, 2, 713, 714],
    [810, 1, 2, 1, 1],
    [1, 1, 2, 2, 2],
    [4, 1, 4, 4, 1014]
]
s.candyCrush(a)

print("-----")


"""
    2nd: simplify the logic in 1st
    - check cols using clone[i][j] == clone[i-1][j] == clone[i-2][j]
    - check rows using clone[i][j] == clone[i][j-1] == clone[i][j-2]
    - use lists to build the new board

    Time    O(kRC) worst case of k = 50/3
    Space   O(RC)
    220 ms, faster than 31.60%
"""


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        R, C = len(board), len(board[0])
        clone = board
        while True:
            toCollapse = set()
            for i in range(R):
                for j in range(C):
                    if clone[i][j] == 0:
                        continue
                    if i-2 >= 0 and clone[i][j] == clone[i-1][j] == clone[i-2][j]:
                        toCollapse.add((i, j))
                        toCollapse.add((i-1, j))
                        toCollapse.add((i-2, j))
                    if j-2 >= 0 and clone[i][j] == clone[i][j-1] == clone[i][j-2]:
                        toCollapse.add((i, j))
                        toCollapse.add((i, j-1))
                        toCollapse.add((i, j-2))
            if len(toCollapse) == 0:
                break
            clone = self.buildBoard(clone, toCollapse)
        return clone

    def buildBoard(self, board, toCollapse):
        # build an array of lists from the bottom for every column
        R, C = len(board), len(board[0])
        nextCols = []
        for j in range(C):
            nextCol = []
            for i in range(R-1, -1, -1):
                if (i, j) not in toCollapse:
                    nextCol.append(board[i][j])
            nextCols.append(nextCol)
        # reassgin the values to a new board
        clone = [C * [0] for _ in range(R)]
        for j in range(C):
            i = R - 1
            col = nextCols[j]
            while len(col) > 0:
                clone[i][j] = col.pop(0)
                i -= 1
        return clone


"""
    3rd: similar to 2nd
    - just transform the board into columns, so the board building process will be easier to manage
"""


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        R, C = len(board), len(board[0])
        cols = self.board2cols(board)
        while True:
            to_collapse = set()
            for j in range(C):
                for i in range(R):
                    cell = cols[j][i]
                    if cell == 0:
                        continue
                    if i+2 < R and cols[j][i] == cols[j][i+1] == cols[j][i+2]:
                        to_collapse.add((i, j))
                        to_collapse.add((i+1, j))
                        to_collapse.add((i+2, j))
                    if j+2 < C and cols[j][i] == cols[j+1][i] == cols[j+2][i]:
                        to_collapse.add((i, j))
                        to_collapse.add((i, j+1))
                        to_collapse.add((i, j+2))
            if len(to_collapse) == 0:
                break
            for i, j in to_collapse:
                cols[j][i] = 0

            for j in range(C):
                zeroIdx = R-1
                # moving zeros
                for i in range(R-1, -1, -1):
                    if cols[j][i] != 0:
                        cols[j][i], cols[j][zeroIdx] = cols[j][zeroIdx], cols[j][i]
                        zeroIdx -= 1

        return self.cols2board(cols)

    def board2cols(self, board):
        R, C = len(board), len(board[0])
        cols = []
        for j in range(C):
            col = []
            for i in range(R):
                col.append(board[i][j])
            cols.append(col)
        return cols

    def cols2board(self, cols):
        C, R = len(cols), len(cols[0])
        rows = []
        for i in range(R):
            row = []
            for j in range(C):
                row.append(cols[j][i])
            rows.append(row)
        return rows
