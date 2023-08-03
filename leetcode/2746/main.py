"""
    DP
    - when we append, we can either append to the front or append to the end

    Learned from others:
    https://leetcode.com/problems/decremental-string-concatenation/solutions/3677531/explained-dp-recursionn/


    Time    O(N * 26 * 26)
    Space   O(N * 26 * 26)
"""


class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        n = len(words)
        res = 2**32

        @lru_cache(None)
        def dfs(i, start, end):
            if i == n:
                return 0
            L1 = len(words[i]) - (end == words[i][0])
            L1 += dfs(i+1, start, words[i][-1])

            L2 = len(words[i]) - (start == words[i][-1])
            L2 += dfs(i+1, words[i][0], end)

            return min(L1, L2)

        return len(words[0]) + dfs(1, words[0][0], words[0][-1])
