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

    def bfs(self, rooms, x, y, steps):
        q = [(x, y, 0)]
        while len(q) > 0:
            i, j, steps = q.pop(0)
            if i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[0]):
                continue
            if rooms[i][j] == -1:
                continue
            # use <= because the staring point == 0
            if steps <= rooms[i][j]:
                rooms[i][j] = steps
                q.append((i-1, j, steps+1))
                q.append((i+1, j, steps+1))
                q.append((i, j-1, steps+1))
                q.append((i, j+1, steps+1))
