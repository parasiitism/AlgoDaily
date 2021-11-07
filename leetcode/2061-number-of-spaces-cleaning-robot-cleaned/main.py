from typing import List

"""
    1st: graph + hashtable
    - clean the floor until hitting a wall
    - once hit, turn 90 degree
    - if the robot visits the same cell again with the same direction, it should stop else it will repeat
"""


class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        R, C = len(room), len(room[0])
        i, j, d = 0, 0, 0
        visited = set()
        res = 1
        room[0][0] = -1

        while True:
            di, dj = dirs[d]

            if 0 <= i + di < R and 0 <= j + dj < C and room[i+di][j+dj] != 1:
                i += di
                j += dj
                if room[i][j] == 0:
                    res += 1
                    room[i][j] = -1
            else:
                d = (d + 1) % 4

            if (i, j, d) in visited:
                return res
            visited.add((i, j, d))


s = Solution()

a = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]

print(s.numberOfCleanRooms(a))

a = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1]]
print(s.numberOfCleanRooms(a))
