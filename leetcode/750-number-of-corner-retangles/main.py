"""
    1st approach: brute force

    Time    O(R(CC + kR)) k: average number of pairs of 1 on each row
    Space   O(k)
    LTE
"""


class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        res = 0
        for i in range(len(grid)):
            pairs = []
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for k in range(j+1, len(grid[0])):
                        if grid[i][k] == 1:
                            pairs.append((j, k))
            for bIdx in range(len(grid)-1, i, -1):
                row = grid[bIdx]
                for x, y in pairs:
                    if row[x] == 1 and row[y] == 1:
                        res += 1
        return res


a = [
    [1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1],
]
print(Solution().countCornerRectangles(a))

a = [
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
]
print(Solution().countCornerRectangles(a))

print("-----")

"""
    2nd approach: dp cache

    here we arrive the pair on each column
    no we are going to see if there are pairs, row[j:k+1], on my top
    by finding from the hashtable
    if yes, the number of pairs on my top is the number of retangles we can form on this row

    e.g. [
        [1, 0, 1],  |           |           |           |
        [1, 0, 1],  | form 1    |           |           |
        [0, 0, 0],  <- no match on this row
        [1, 0, 1],              | form 2    |           |
        [1, 0, 1],                          | form 3    |
        [1, 0, 1],                                      | form 4
    ]
    on each layer, we can form number of retangles if there are pairs on the same position on my top
    so the total count of retangles = 1 + 2 + 3 + 4 = 10

    Time    O(RCC)
    Space   O(CC)
    1404 ms, faster than 47.73%
"""


class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        res = 0
        m = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for k in range(j+1, len(grid[0])):
                        if grid[i][k] == 1:
                            # here we arrive the pair on each column
                            # no we are going to see if there are pairs, row[j:k+1], on my top
                            # by finding from the hashtable
                            # if yes, the number of pairs on my top is the number of retangles we can form on this row
                            key = str(j) + ',' + str(k)
                            if key in m:
                                res += m[key]
                                m[key] += 1
                            else:
                                m[key] = 1
                            print(m)
        return res


a = [
    [1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1],
]
print(Solution().countCornerRectangles(a))

a = [
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
]
print(Solution().countCornerRectangles(a))

a = [
    [1, 0, 1],
    [0, 0, 0],
    [1, 0, 1],
]
print(Solution().countCornerRectangles(a))

"""
    followup: max area amongst the corner retangles
"""


class Solution(object):
    def maxAreaCornerRectangle(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            pairs = []
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for k in range(j+1, len(grid[0])):
                        if grid[i][k] == 1:
                            pairs.append((j, k))
            for bIdx in range(len(grid)-1, i, -1):
                row = grid[bIdx]
                for x, y in pairs:
                    if row[x] == 1 and row[y] == 1:
                        area = (y-x+1)*(bIdx-i+1)
                        res = max(res, area)
        return res
