"""
    DFS + hashtable
    - we can use a hashtable to avoid revisit
    - to avoid a cell being visited by another exploration(e.g. BFS), we should use DFS. i.e. replore a path 1 by 1

    Time    O(RC)
    Space   O(RC)
    3552 ms, faster than 61.33% 
"""


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        R, C = len(grid), len(grid[0])
        seen = set()

        def dfs(_i, _j, target_char):
            stack = [(_i, _j, 0, None)]
            while len(stack) > 0:
                i, j, steps, prev = stack.pop()
                if i < 0 or i == R or j < 0 or j == C:
                    continue
                if grid[i][j] != target_char:
                    continue
                key = (i, j)
                if key in seen:
                    if steps >= 4:
                        return True
                    continue
                seen.add(key)
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if (i+di, j+dj) == prev:
                        continue
                    stack.append((i+di, j+dj, steps + 1, key))
            return False

        for i in range(R):
            for j in range(C):
                if (i, j) in seen:
                    continue
                if dfs(i, j, grid[i][j]):
                    return True
        return False
