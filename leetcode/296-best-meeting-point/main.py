import sys

"""
    1st approach: bfs + hashtable
    - for each person, bfs to count the distance on the distance board
    
    Time    O(rrcc)
    Space   O(rrcc)
    LTE
"""


class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        distanceBoard = []
        for _ in grid:
            distanceBoard.append(len(grid[0])*[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.bfs(distanceBoard, grid, i, j)
        minDist = sys.maxsize
        minI = -1
        minJ = -1
        for i in range(len(distanceBoard)):
            for j in range(len(distanceBoard[0])):
                if distanceBoard[i][j] < minDist:
                    minDist = distanceBoard[i][j]
                    minI, minJ = i, j
        # return minI, minJ, minDist
        return minDist

    def bfs(self, distanceBoard, origBoard, x, y):
        seen = []
        for _ in origBoard:
            seen.append(len(origBoard[0])*[False])

        q = []
        q.append((x, y, 0))
        while len(q) > 0:
            i, j, steps = q.pop(0)
            if i < 0 or i+1 > len(origBoard) or j < 0 or j+1 > len(origBoard[0]):
                continue
            if seen[i][j] == True:
                continue
            seen[i][j] = True
            distanceBoard[i][j] += steps
            q.append((i-1, j, steps+1))
            q.append((i+1, j, steps+1))
            q.append((i, j-1, steps+1))
            q.append((i, j+1, steps+1))


a = [
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
]

print(Solution().minTotalDistance(a))

print("-----")
