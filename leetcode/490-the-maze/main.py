"""
    1st approach: BFS
    - similar to lc505, 562
    - if the ball hits the wall, try to roll in 4 directions until the explorations hit the wall
    - only cache the pivot points where we turned(in front of the wall)

    Time    O(RC)
    Space    O(RC)
    272 ms, faster than 48.96%
"""


class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        # left, right, up, down
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        # destination
        destI, destJ = destination[0], destination[1]
        visited = {}

        q = []
        q.append((start[0], start[1]))

        while len(q) > 0:
            i, j = q.pop(0)
            if i == destI and j == destJ:
                return True

            for di, dj in dirs:
                # roll the ball until it hits a wall
                row = i
                col = j
                while 0 <= row+di < len(maze) and 0 <= col+dj < len(maze[0]) and maze[row+di][col+dj] == 0:
                    row += di
                    col += dj
                # check if the new starting position has been visited
                key = str(row) + "," + str(col)
                if key in visited:
                    continue
                visited[key] = True
                q.append((row, col))
        return False


a = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
b = [0, 4]
c = [4, 4]
print(Solution().hasPath(a, b, c))

a = [
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
b = [0, 4]
c = [4, 4]
print(Solution().hasPath(a, b, c))

a = [
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
b = [0, 4]
c = [4, 4]
print(Solution().hasPath(a, b, c))

print("----------")

"""
    2nd approach: DFS
    - similar to lc505, 562
    - if the ball hits the wall, try to roll in 4 directions until the explorations hit the wall
    - only cache the pivot points where we turned(in front of the wall)

    Time    O(RC)
    Space    O(RC)
    272 ms, faster than 48.96%
"""


class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        # left, right, up, down
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        # destination
        destI, destJ = destination[0], destination[1]
        visited = {}

        def dfs(i, j):
            if i == destI and j == destJ:
                return True
            for di, dj in dirs:
                # roll the ball until it hits a wall
                row = i
                col = j
                while 0 <= row+di < len(maze) and 0 <= col+dj < len(maze[0]) and maze[row+di][col+dj] == 0:
                    row += di
                    col += dj
                # check if the new starting position has been visited
                key = str(row) + "," + str(col)
                if key in visited:
                    continue
                visited[key] = True
                if dfs(row, col):
                    return True
            return False

        return dfs(start[0], start[1])


a = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
b = [0, 4]
c = [4, 4]
print(Solution().hasPath(a, b, c))

a = [
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
b = [0, 4]
c = [4, 4]
print(Solution().hasPath(a, b, c))

a = [
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
b = [0, 4]
c = [4, 4]
print(Solution().hasPath(a, b, c))
