import sys
import heapq

"""
    1st approach: bfs + heap + hashtable
    - the heap always maintain the symbols with minsteps
    - bfs for each symbol, bfs through the possibilities
    - if there is a ladder or snake, directly enqueue the next symbol
    - use a hashtbale to store visited cells

    Time    O(mnlog(mn)) the heap
    Space   O(n) the heap + seen + lookup
    236 ms, faster than 8.66%
"""


class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        lookup = self.generateBoardIndeces(board)
        # seen
        seen = []
        for _ in range(len(board)):
            seen.append(len(board[0]) * [False])
        # bfs
        q = []
        # q = [[steps, symbol], ...]
        heapq.heappush(q, (0, 1))
        while len(q) > 0:
            n = len(q)
            # dequeue
            steps, symbol = heapq.heappop(q)
            i, j = lookup[symbol]
            # skip seen
            if seen[i][j]:
                continue
            seen[i][j] = True
            # destination
            if symbol == len(board)*len(board):
                return steps
            # dice x+1, x+2..., x+6
            for k in range(1, 7):
                if symbol+k in lookup:
                    nxt = symbol+k
                    x, y = lookup[nxt]
                    # if we see a snake or ladder, use the short cut
                    if board[x][y] != -1:
                        nxt = board[x][y]
                    # enqueue
                    heapq.heappush(q, (steps+1, nxt))

        return -1

    def generateBoardIndeces(self, board):
        # generate and reverse odd cols
        dump = []
        count = 1
        for i in range(len(board)):
            temp = []
            for j in range(len(board[0])):
                if i % 2 == 0:
                    temp.append(count)
                else:
                    temp.insert(0, count)
                count += 1
            dump.append(temp)
        # reverse rows
        up = 0
        down = len(dump)-1
        while up < down:
            dump[up], dump[down] = dump[down], dump[up]
            up += 1
            down -= 1
        # build lookup table
        lookup = {}
        for i in range(len(dump)):
            for j in range(len(dump[0])):
                lookup[dump[i][j]] = (i, j)
        return lookup


a = [
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 35, -1, -1, 13, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 15, -1, -1, -1, -1],
]
"""
[[36, 35, 34, 33, 32, 31], 
[25, 26, 27, 28, 29, 30], 
[24, 23, 22, 21, 20, 19], 
[13, 14, 15, 16, 17, 18], 
[12, 11, 10, 9, 8, 7], 
[1, 2, 3, 4, 5, 6]]
"""
print(Solution().snakesAndLadders(a))

a = [
    [-1, 1, 2, -1],
    [2, 13, 15, -1],
    [-1, 10, -1, -1],
    [-1, 6, 2, 8],
]
"""
[[16, 15, 14, 13], 
[9, 10, 11, 12], 
[8, 7, 6, 5], 
[1, 2, 3, 4]]
"""
print(Solution().snakesAndLadders(a))

print("-----")

"""
    2nd approach: bfs + hashtable
    - SINCE we are doing bfs and we move forward the symbols with ladders/snakes, 
        the shortest path must be the first one who arrives at the destination
    - bfs for each symbol, bfs through the possibilities
    - if there is a ladder or snake, directly enqueue the next symbol
    - use a hashtbale to store visited cells

    Time    O(mn)
    Space   O(n) the seen + lookup
    140 ms, faster than 39.56%
"""


class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        lookup = self.generateBoardIndeces(board)
        # set to avoid redundancy
        seen = set()
        # bfs
        q = []
        # [(symbol, steps),...]
        q.append((1, 0))
        while len(q) > 0:
            n = len(q)
            # dequeue
            symbol, steps = q.pop(0)
            # skip seen
            if symbol in seen:
                continue
            seen.add(symbol)
            # destination
            if symbol == len(board)*len(board):
                return steps
            # snake, ladder or nothing
            # dice x+1, x+2..., x+6
            for delta in range(1, 7):
                if symbol+delta in lookup:
                    nextSymbol = symbol+delta
                    x, y = lookup[nextSymbol]
                    # snake or ladder
                    if board[x][y] != -1:
                        q.append((board[x][y], steps+1))
                    else:
                        q.append((nextSymbol, steps+1))

        return -1

    def generateBoardIndeces(self, board):
        # generate and reverse the odd cols
        dump = []
        count = 1
        for i in range(len(board)):
            temp = []
            for j in range(len(board[0])):
                if i % 2 == 0:
                    temp.append(count)
                else:
                    temp.insert(0, count)
                count += 1
            dump.append(temp)
        # reverse the rows
        up = 0
        down = len(dump)-1
        while up < down:
            dump[up], dump[down] = dump[down], dump[up]
            up += 1
            down -= 1
        # build lookup table
        lookup = {}
        for i in range(len(dump)):
            for j in range(len(dump[0])):
                lookup[dump[i][j]] = (i, j)
        return lookup


a = [
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 35, -1, -1, 13, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 15, -1, -1, -1, -1],
]
"""
[[36, 35, 34, 33, 32, 31], 
[25, 26, 27, 28, 29, 30], 
[24, 23, 22, 21, 20, 19], 
[13, 14, 15, 16, 17, 18], 
[12, 11, 10, 9, 8, 7], 
[1, 2, 3, 4, 5, 6]]
"""
print(Solution().snakesAndLadders(a))

a = [
    [-1, 1, 2, -1],
    [2, 13, 15, -1],
    [-1, 10, -1, -1],
    [-1, 6, 2, 8],
]
"""
[[16, 15, 14, 13], 
[9, 10, 11, 12], 
[8, 7, 6, 5], 
[1, 2, 3, 4]]
"""
print(Solution().snakesAndLadders(a))
