"""
    hashtable

    Time    O(N)
    Space   O(4N)
    3444 ms, faster than 58.33%
"""


class Solution:
    def countUnguarded(self, R: int, C: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        explored = set()
        for i, j in walls:
            explored.add((i, j, 'up'))
            explored.add((i, j, 'down'))
            explored.add((i, j, 'left'))
            explored.add((i, j, 'right'))
        for i, j in guards:
            explored.add((i, j, 'up'))
            explored.add((i, j, 'down'))
            explored.add((i, j, 'left'))
            explored.add((i, j, 'right'))
            for _i in range(i-1, -1, -1):
                if (_i, j, 'up') in explored:
                    break
                explored.add((_i, j, 'up'))
            for _j in range(j-1, -1, -1):
                if (i, _j, 'left') in explored:
                    break
                explored.add((i, _j, 'left'))
            for _i in range(i+1, R):
                if (_i, j, 'down') in explored:
                    break
                explored.add((_i, j, 'down'))
            for _j in range(j+1, C):
                if (i, _j, 'right') in explored:
                    break
                explored.add((i, _j, 'right'))
        res = 0
        for i in range(R):
            for j in range(C):
                if (i, j, 'up') in explored or (i, j, 'down') in explored or (i, j, 'left') in explored or (i, j, 'right') in explored:
                    continue
                res += 1
        return res
