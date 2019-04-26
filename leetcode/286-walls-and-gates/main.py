"""
    1st approach: dfs

	Time	O(N)
	Space	O(h)
    384 ms, faster than 35.34%
"""


class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.dfs(rooms, i, j, 0)

    def dfs(self, rooms, i, j, steps):
        if i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[0]):
            return
        if rooms[i][j] == -1:
            return
        # if we revisit to a certain cell, the steps must be larger therefore we can avoid redundant calculation
        # without using a hashtable/set
        if steps <= rooms[i][j]:
            rooms[i][j] = steps
            self.dfs(rooms, i-1, j, steps + 1)
            self.dfs(rooms, i+1, j, steps + 1)
            self.dfs(rooms, i, j-1, steps + 1)
            self.dfs(rooms, i, j+1, steps + 1)


"""
    2nd approach: bfs

	Time	O(N)
	Space	O(h)
    384 ms, faster than 35.34%
"""


class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.bfs(rooms, i, j, 0)

    def bfs(self, rooms, i, j, steps):
        if i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[0]):
            return
        q = [(i, j, 0)]
        while len(q) > 0:
            x, y, steps = q.pop(0)
            if rooms[x][y] == -1:
                continue
            if steps <= rooms[x][y]:
                rooms[x][y] = steps
                if x-1 >= 0:
                    q.append((x-1, y, steps+1))
                if x+1 < len(rooms):
                    q.append((x+1, y, steps+1))
                if y-1 >= 0:
                    q.append((x, y-1, steps+1))
                if y+1 < len(rooms[0]):
                    q.append((x, y+1, steps+1))
