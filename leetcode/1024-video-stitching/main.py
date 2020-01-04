import sys

"""
    1st: dynamic programming, learned from others
    - the basic idea is to construct an array to store the minimum number of stitchs on every timestamp
    
    e.g.
    clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]]
    T = 9

    We can take clips [0,4], [4,7], and [6,9]
    [1, 1, 1, 1, 1, 2, 2, 2, 3, 3]

    ref:
    - https://leetcode.com/problems/video-stitching/discuss/270036/JavaC%2B%2BPython-Greedy-Solution-O(1)-Space

    Time    O(NT)
    Space   O(T)
    28 ms, faster than 19.38%
"""
class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        dp = (T + 1) * [sys.maxsize]
        dp[0] = 0
        for i in range(T + 1):
            for start, end in clips:
                if start <= i <= end:
                    dp[i] = min(dp[start] + 1, dp[i])
        if dp[T] == sys.maxsize:
            return -1
        return dp[T]

s = Solution()

a = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]]
b = 9
print(s.videoStitching(a, b))