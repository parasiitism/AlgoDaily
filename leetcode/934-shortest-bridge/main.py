import sys

"""
    1st: brute force BFS
    - paint all the cells of one island to be another color
    - for each cell in painteds, find the shortet way to the cell with original color

    90 / 96 test cases passed LTE
"""


class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        found = False
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 1 and found == False:
                    self.paint(A, i, j)
                    found = True
                    break
            if found:
                break
        res = sys.maxsize
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 2:
                    steps = self.bfs(A, i, j, res)
                    res = min(res, steps-1)
        return res

    def paint(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
            return
        if A[i][j] == 1:
            A[i][j] = 2
            self.paint(A, i-1, j)
            self.paint(A, i+1, j)
            self.paint(A, i, j-1)
            self.paint(A, i, j+1)

    def bfs(self, A, start_i, start_j, res):
        q = [(start_i, start_j, 0)]
        hs = set()
        while len(q) > 0:
            i, j, steps = q.pop(0)
            if (i, j) in hs:
                continue
            hs.add((i, j))
            if A[i][j] == 1:
                return steps
            if steps > res:
                return sys.maxsize
            if i-1 >= 0 and (A[i-1][j] == 0 or A[i-1][j] == 1):
                q.append((i-1, j, steps+1))
            if i+1 < len(A) and (A[i+1][j] == 0 or A[i+1][j] == 1):
                q.append((i+1, j, steps+1))
            if j-1 >= 0 and (A[i][j-1] == 0 or A[i][j-1] == 1):
                q.append((i, j-1, steps+1))
            if j+1 < len(A[0]) and (A[i][j+1] == 0 or A[i][j+1] == 1):
                q.append((i, j+1, steps+1))
        return sys.maxsize


s = Solution()

a = [[0, 1], [1, 0]]
print(s.shortestBridge(a))

a = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
print(s.shortestBridge(a))

a = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [
    1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
print(s.shortestBridge(a))


a = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 1], [
    0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
print(s.shortestBridge(a))

print("-----")

"""
    1st: optimize DFS + BFS
    - paint all the cells of one island to be another color
    - only record the cells that is on the boundary of the first island
    - for each cell on boundary, find the shortet way to the cell with original color

    Time    O(RCk) -> O(RCRC) depends on the shape of the islands
    Space   O(RC)
    1492 ms, faster than 5.06%
"""


class Solution(object):

    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        self.edges = set()
        found = False
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 1 and found == False:
                    self.paint_and_find_edges(A, i, j)
                    found = True
                    break
            if found:
                break
        res = sys.maxsize
        for i, j in self.edges:
            steps = self.bfs(A, i, j, res)
            res = min(res, steps-1)
        return res

    def paint_and_find_edges(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
            return
        if A[i][j] == 1:
            A[i][j] = 2
            if i-1 >= 0 and A[i-1][j] == 0:
                self.edges.add((i, j))
            elif i+1 < len(A) and A[i+1][j] == 0:
                self.edges.add((i, j))
            elif j-1 >= 0 and A[i][j-1] == 0:
                self.edges.add((i, j))
            elif j+1 < len(A[0]) and A[i][j+1] == 0:
                self.edges.add((i, j))
            self.paint_and_find_edges(A, i-1, j)
            self.paint_and_find_edges(A, i+1, j)
            self.paint_and_find_edges(A, i, j-1)
            self.paint_and_find_edges(A, i, j+1)

    def bfs(self, A, start_i, start_j, res):
        q = [(start_i, start_j, 0)]
        hs = set()
        while len(q) > 0:
            i, j, steps = q.pop(0)
            if (i, j) in hs:
                continue
            hs.add((i, j))
            if A[i][j] == 1:
                return steps
            if steps > res:
                return sys.maxsize
            if i-1 >= 0 and (A[i-1][j] == 0 or A[i-1][j] == 1):
                q.append((i-1, j, steps+1))
            if i+1 < len(A) and (A[i+1][j] == 0 or A[i+1][j] == 1):
                q.append((i+1, j, steps+1))
            if j-1 >= 0 and (A[i][j-1] == 0 or A[i][j-1] == 1):
                q.append((i, j-1, steps+1))
            if j+1 < len(A[0]) and (A[i][j+1] == 0 or A[i][j+1] == 1):
                q.append((i, j+1, steps+1))
        return sys.maxsize


s = Solution()

a = [[0, 1], [1, 0]]
print(s.shortestBridge(a))

a = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
print(s.shortestBridge(a))

a = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [
    1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
print(s.shortestBridge(a))


a = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]
print(s.shortestBridge(a))

a = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,1,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
print(s.shortestBridge(a))