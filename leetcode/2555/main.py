"""
    1st: Dynamic programming (bottom-up)
    - learned from others
    https://leetcode.com/problems/maximize-win-from-two-segments/solutions/3141449/java-c-python-dp-sliding-segment-o-n/?orderBy=most_votes

    Time    O(N)
    Space   O(N)
"""


class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        dp = (n + 1) * [0]
        j = 0
        res = 0
        for i in range(n):
            while prizePositions[j] < prizePositions[i] - k:
                j += 1
            length = i - j + 1
            # so dp[i] stores the maximum length from 0th to i-1th
            dp[i+1] = max(dp[i], length)
            res = max(res, length + dp[j])
        return res


"""
    2nd: Dynamic programming (up-down)
    - with this approach, we can also solve the follow-up where segments >= 2

    Time    O(N)
    Space   O(2N)
"""


class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)

        cache = {}

        def dfs(i, seg):
            if seg == 0 or i == n:
                return 0
            key = (i, seg)
            if key in cache:
                return cache[key]
            j = bisect.bisect_right(prizePositions, prizePositions[i] + k)
            count = j - i

            consider = count + dfs(j, seg-1)
            skip = dfs(i+1, seg)
            cache[key] = max(consider, skip)
            return cache[key]

        return dfs(0, 2)
