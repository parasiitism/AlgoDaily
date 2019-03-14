import heapq

"""
    questions to ask:
    - start from (0,0)? yes
    - heights are different? yes
    - the forest is guaranteed to be a retangle? no nodge? yes

    potential follow-ups:
    - start from any point
    - some heights equal
"""

"""
    1st approach:
    1. put all the nodes into a priority queue, sort them by height
    2. pop the pq and calculate the steps between each node, as well as the starting point
    3. bfs through the forest to calculate the steps

    Time    O(M*N + TlogT + TlogT*M*N)
    10896 ms, faster than 5.58%
"""


class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        if len(forest) == 0 or len(forest[0]) == 0:
            return -1
        # put all the nodes into a priority queue, sort them by height
        pq = []
        for i in range(len(forest)):
            for j in range(len(forest[i])):
                if forest[i][j] > 1:
                    heapq.heappush(pq, (forest[i][j], i, j))
        # pop the pq and calculate the steps between each node, as well as the starting point
        totalSteps = 0
        curPos = [0, 0]
        while len(pq) > 0:
            h, i, j = heapq.heappop(pq)
            steps = self.bfs(curPos, forest, i, j)
            if steps == -1:
                return -1
            totalSteps += steps
            curPos = [i, j]
        return totalSteps

    def bfs(self, curPos, forest, targetI, targetJ):
        # 2d array for visited nodes
        visited = []
        for i in range(len(forest)):
            temp = []
            for j in range(len(forest[i])):
                temp.append(False)
            visited.append(temp)
        # bfs through the forest
        q = []
        q.append((curPos[0], curPos[1], 0))  # i, j, steps
        while len(q) > 0:
            i, j, steps = q.pop(0)
            # check boundaries
            if i < 0 or i+1 > len(forest) or j < 0 or j+1 > len(forest[0]):
                continue
            # check if visited
            # print(i, j, len(visited), len(visited[0]))
            if visited[i][j] == True:
                continue
            visited[i][j] = True
            # check if reach
            if i == targetI and j == targetJ:
                return steps
            elif forest[i][j] >= 1:
                q.append((i-1, j, steps+1))
                q.append((i, j-1, steps+1))
                q.append((i+1, j, steps+1))
                q.append((i, j+1, steps+1))

        return -1


a = [
    [1, 2, 3],
    [0, 0, 4],
    [7, 6, 5],
]
print(Solution().cutOffTree(a))

a = [
    [1, 2, 3],
    [0, 0, 0],
    [7, 6, 5],
]
print(Solution().cutOffTree(a))

a = [
    [2, 3, 4],
    [0, 0, 5],
    [8, 7, 6],
]
print(Solution().cutOffTree(a))

a = [
    [1, 0],
    [3, 2],
]
print(Solution().cutOffTree(a))

a = [
    [1, 3, 0, 2],
    [1, 1, 3, 1],
]
print(Solution().cutOffTree(a))


print("-----")

"""
    2nd approach:
    1. sort the trees by height
    2. pop the pq and calculate the steps between each node, as well as the starting point
    3. bfs through the forest to calculate the steps

    Time    O(M*N + TlogT + T*M*N)
    10024 ms, faster than 5.40%
"""


class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        if len(forest) == 0 or len(forest[0]) == 0:
            return -1
        # sort the trees by height
        trees = []
        for i in range(len(forest)):
            for j in range(len(forest[i])):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))
        trees = sorted(trees, key=lambda x: x[0])
        # pop the arr and calculate the steps between each node, start from the starting point
        totalSteps = 0
        curPos = [0, 0]
        while len(trees) > 0:
            h, i, j = trees.pop(0)
            steps = self.bfs(curPos, forest, i, j)
            if steps == -1:
                return -1
            totalSteps += steps
            curPos = [i, j]
        return totalSteps

    def bfs(self, curPos, forest, targetI, targetJ):
        # 2d array for visited nodes
        visited = []
        for i in range(len(forest)):
            temp = len(forest[i])*[False]
            visited.append(temp)
        # bfs through the forest
        q = []
        q.append((curPos[0], curPos[1], 0))  # i, j, steps
        while len(q) > 0:
            i, j, steps = q.pop(0)
            # check boundaries
            if i < 0 or i+1 > len(forest) or j < 0 or j+1 > len(forest[0]):
                continue
            # check if visited
            if visited[i][j] == True:
                continue
            visited[i][j] = True
            # check if reach
            if i == targetI and j == targetJ:
                return steps
            elif forest[i][j] >= 1:
                q.append((i-1, j, steps+1))
                q.append((i, j-1, steps+1))
                q.append((i+1, j, steps+1))
                q.append((i, j+1, steps+1))

        return -1


a = [
    [1, 2, 3],
    [0, 0, 4],
    [7, 6, 5],
]
print(Solution().cutOffTree(a))

a = [
    [1, 2, 3],
    [0, 0, 0],
    [7, 6, 5],
]
print(Solution().cutOffTree(a))

a = [
    [2, 3, 4],
    [0, 0, 5],
    [8, 7, 6],
]
print(Solution().cutOffTree(a))

a = [
    [1, 0],
    [3, 2],
]
print(Solution().cutOffTree(a))

a = [
    [1, 3, 0, 2],
    [1, 1, 3, 1],
]
print(Solution().cutOffTree(a))
