"""
    1st: bfs
    
    Time    O(RC)
    Space   O(RC)
    1744 ms, faster than 30.00%
"""


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        R, C = len(land), len(land[0])
        self.seen = set()
        res = []
        for i in range(R):
            for j in range(C):
                if land[i][j] == 1 and (i, j) not in self.seen:
                    _i, _j = self.bfs(land, i, j)
                    res.append([i, j, _i, _j])
        return res

    def bfs(self, land, x, y):
        R, C = len(land), len(land[0])
        maxCoor = (x+y, x, y)
        q = [(x, y)]
        while len(q) > 0:
            i, j = q.pop(0)
            if i < 0 or i == R or j < 0 or j == C:
                continue
            if land[i][j] != 1:
                continue
            key = (i, j)
            if key in self.seen:
                continue
            self.seen.add(key)

            if i+j > maxCoor[0]:
                maxCoor = (i+j, i, j)

            q.append((i-1, j))
            q.append((i+1, j))
            q.append((i, j-1))
            q.append((i, j+1))
        return maxCoor[1], maxCoor[2]
