import sys
import heapq

"""
    1st: dynamic programming, recursive bottom up + memoization
    - basically traverse all the paths, add up the values from the bottom
    - cache the running sum(from the bottom) to avoid redundant calculation
    Time    O(RCC)
    Space   O(RC)
    TLE
    TLE     9/13
"""


class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        self.ht = {}
        cost = sys.maxsize
        for j in range(len(A[0])):
            cost = min(cost, self.dfs(A, 0, j))
        return cost

    def dfs(self, A, i, j):
        if i + 1 == len(A):
            return A[i][j]
        if (i, j) in self.ht:
            return self.ht[(i, j)]

        cost = sys.maxsize
        for idx in range(len(A[i])):
            if idx != j:
                cost = min(cost, self.dfs(A, i+1, idx) + A[i][j])

        self.ht[(i, j)] = cost
        return cost


"""
    2nd: dynamic programming, bottom up
    - storing the minimum running sum from bottom of the matrix
    Time    O(RCC)
    Space   O(RC)
    TLE     11/13
"""


class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for i in range(len(A)-2, -1, -1):
            for j in range(len(A[0])):
                best = sys.maxsize
                for k in range(len(A[0])):
                    if k != j:
                        best = min(best, A[i+1][k])
                A[i][j] += best
        res = sys.maxsize
        for j in range(len(A[0])):
            res = min(res, A[0][j])
        return res


"""
    3rd: dynamic programming + sort
    - learned from others
    - sort the matrix row by row
    - add up the minimum value and the 2nd minimum value to each cell on next row. e.g. lc256 paint house

    ref:
    - https://leetcode.com/problems/minimum-falling-path-sum-ii/discuss/451273/Python-DP-O(MN)

    Time    O(RC * logC)
    Space   O(C)
    236 ms, faster than 68.06%
"""


class Solution(object):
    def minFallingPathSum(self, A):
        for i in range(1, len(A)):
            r = heapq.nsmallest(2, A[i - 1])
            for j in range(len(A[0])):
                # add the smallest item on the previous row
                # it can only either be the smallest or the 2nd smallest
                if A[i - 1][j] == r[0]:
                    # if the above item is smallest, add up with the 2nd smallest
                    A[i][j] += r[1]
                else:
                    # if the above item is not thes smallest, add up with the smallest
                    A[i][j] += r[0]
        return min(A[-1])


s = Solution()
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(s.minFallingPathSum(a))
