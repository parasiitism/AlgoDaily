"""
    1st: dynamic programming(DP)
    - come up with prefixsum in a DP way
    - binary search the upper bound of the result(the length of square)

    ref:
    - https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/discuss/451871/Java-sum%2Bbinary-O(m*n*log(min(mn)))-or-sum%2Bsliding-window-O(m*n)
    - https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/discuss/451898/Python-Clean-code-PrefixSum-and-BinarySearch-in-O(m*n*log(min(mn)))
    - https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/discuss/451998/Python3-prefix-sum-and-binary-search

    Time    O(MN log MN)
    Space   O(MN)
    876 ms, faster than 84.39%
"""


class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        m, n = len(mat), len(mat[0])

        # prefixsum matrix
        prefix = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - \
                    prefix[i-1][j-1] + mat[i-1][j-1]

        # function for binary search
        def below(k):
            """reture true if there is such a sub-matrix of length k"""
            for i in range(k, m+1):
                for j in range(k, n+1):
                    if prefix[i][j] - prefix[i-k][j] - prefix[i][j-k] + prefix[i-k][j-k] <= threshold:
                        return True
            return False

        # binary search
        low, high = 1, min(m, n)
        while low <= high:
            mid = (low + high)/2
            if below(mid):
                low = mid + 1
            else:
                high = mid - 1

        return high
