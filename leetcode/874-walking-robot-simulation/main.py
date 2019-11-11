"""
    1st: brute force
    - basically we just have to check the next cell every time we talk 

    Time    O(N+K)
    Space   O(K)
    328 ms, faster than 56.67%
"""


class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x, y = 0, 0
        direction = 0
        obstacleSet = set([(i, j) for i, j in obstacles])
        ans = 0

        for cmd in commands:
            if cmd == -2:  # left
                direction = (direction - 1) % 4
            elif cmd == -1:  # right
                direction = (direction + 1) % 4
            else:
                for _ in range(cmd):
                    if (x + dx[direction], y + dy[direction]) not in obstacleSet:
                        x += dx[direction]
                        y += dy[direction]
                        ans = max(ans, x*x + y*y)
        return ans
