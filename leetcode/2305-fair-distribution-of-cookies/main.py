"""
    Recursion
    - try all possibilities
    - to speed up, prune the recursion tree

    Time    O(N^N)
    Space   O(N^N)
    1272 ms, faster than 25.00% 
"""


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        self.diff = 2**32
        self.res = 2**32

        def dfs(idx, bags):
            if idx == n:
                min_val = 2**32
                max_val = 0
                for b in bags:
                    min_val = min(min_val, b)
                    max_val = max(max_val, b)
                if min_val <= 0:
                    return
                diff = max_val - min_val
                if diff < self.diff:
                    self.res = max_val
                    self.diff = diff
                return

            # prune the dfs branches
            if max(bags) >= self.res:
                return

            for i in range(k):
                clone = bags[:]
                clone[i] += cookies[idx]
                dfs(idx+1, clone)
        dfs(0, k*[0])
        return self.res
