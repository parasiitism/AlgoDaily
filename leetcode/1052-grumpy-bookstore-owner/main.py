"""
    1st: prefixsum + sliding window
    - come up with prefixSums and suffixSums
    - the result must be the maximum among all the prefixSums[before] + windowSum + suffixSums[after]

    Time    O(n)
    Space   O(2n)
    300 ms, faster than 17.32%
"""
class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        if len(customers) == 0 or len(grumpy) == 0 or len(customers) != len(grumpy):
            return 0
        N = len(customers)
        prefixSums = N * [0]
        suffixSums = N * [0]
        
        pfs = 0
        for i in range(N):
            if grumpy[i] == 0:
                pfs += customers[i]
            prefixSums[i] = pfs
        sfs = 0
        for i in range(N-1, -1, -1):
            if grumpy[i] == 0:
                sfs += customers[i]
            suffixSums[i] = sfs
        
        windowSum = sum(customers[:X])
        res = windowSum + (suffixSums[X] if X < N else 0)
        for i in range(X, N):
            windowSum -= customers[i-X]
            windowSum += customers[i]
            temp = prefixSums[i-X] + windowSum
            if i+1 < N:
                temp += suffixSums[i+1]
            res = max(res, temp)
        return res
            