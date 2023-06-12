"""
    DFS, recursion
    - balance the costs at every node
    
    My 1st approach was to find the max_cost at every level, but it was incorrect, let's see this corner case:
    ---- 2
    --- 3 4
    - 5 5 4 4

    Time    O(N)
    Space   O(logN)
"""


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:

        total = 0

        def dfs(node):
            nonlocal total
            if node > len(cost):
                return 0
            left = dfs(node*2)
            right = dfs(node*2+1)
            total += abs(left - right)
            return max(left, right) + cost[node-1]

        dfs(1)
        return total
