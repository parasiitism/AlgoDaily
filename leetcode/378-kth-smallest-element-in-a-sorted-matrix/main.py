import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int

        1st approach: heap

        Time    O(nlogn)
        Space   O(n)
        244 ms, faster than 15.37%
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return None
        hq = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                heapq.heappush(hq, matrix[i][j])
        res = None
        for i in range(k):
            res = heapq.heappop(hq)
        return res
