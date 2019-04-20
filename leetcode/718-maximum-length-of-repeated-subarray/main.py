"""
    1st approach: Longest Common Substring

    Time    O(AB)
    Space   O(AB)
    3916 ms beats 30%
"""


class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if len(A) == 0 or len(B) == 0:
            return 0
        dp = []
        for i in range(len(A)):
            dp.append(len(B)*[0])
        res = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    if i-1 >= 0 and j-1 >= 0:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = 1
                    res = max(res, dp[i][j])
        return res


a = [1, 2, 3, 2, 1]
b = [3, 2, 1, 4, 7]
print(Solution().findLength(a, b))
