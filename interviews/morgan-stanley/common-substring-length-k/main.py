"""
    Check whether there exists a common substring of length of k between 2 given strings

    classic approach: longest common substring variation

    followup: print the substring as well 

    Time    O(AB)
    Space   O(AB)
    3916 ms beats 30%
"""


class Solution(object):
    def findLength(self, A, B, k):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if len(A) == 0 or len(B) == 0:
            return 0
        # dp array for subproblems
        dp = []
        for i in range(len(A)):
            dp.append(len(B)*[0])
        # dp
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    # extend the commong substring we found previously
                    if i >= 1 and j >= 1:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = 1
                    # check if == k
                    if dp[i][j] == k:
                        return True
        return False


# 3
a = "ABCBA"
b = "CBADG"
print(Solution().findLength(a, b, 2))
print(Solution().findLength(a, b, 3))
print(Solution().findLength(a, b, 4))
print("----")

# 6
a = "cdabxyzccznmotuv"
b = "aabzdazccznmvvtcdabx"
print(Solution().findLength(a, b, 3))
print(Solution().findLength(a, b, 4))
print(Solution().findLength(a, b, 5))
print(Solution().findLength(a, b, 6))
print(Solution().findLength(a, b, 7))
