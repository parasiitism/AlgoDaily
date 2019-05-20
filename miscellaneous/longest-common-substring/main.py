"""
    classic approach: Longest Common Substring

    followup: print the substring as well 

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
        resStr = ""
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    if i >= 1 and j >= 1:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = 1
                    if dp[i][j] > res:
                        res = dp[i][j]
                        resStr = A[i-res+1:i+1]
        print(resStr)
        return res


a = "ABCBA"
b = "CBADG"
print(Solution().findLength(a, b))
