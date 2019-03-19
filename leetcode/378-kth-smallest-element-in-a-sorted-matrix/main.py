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
        arr = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                arr.append(matrix[i][j])
        arr = sorted(arr)
        return arr[k-1]


a = [
    [1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
]
print(Solution().kthSmallest(a, 8))
