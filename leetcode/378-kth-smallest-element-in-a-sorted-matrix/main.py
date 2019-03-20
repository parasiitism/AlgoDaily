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
        48 ms, faster than 73.06%
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


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int

        1st approach: max heap
        - use a max heap with limited capacity k
        - when we meet a new element and the heap overflows, 
        we pop the toppest element such that we can maintain the heap contains the k smallest elements only

        Time    O(nlogn)
        Space   O(n)
        248 ms, faster than 14.97%
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return None
        arr = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                heapq.heappush(arr, -matrix[i][j])
                if len(arr) > k:
                    heapq.heappop(arr)
        return -arr[0]


a = [
    [1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
]
print(Solution().kthSmallest(a, 8))
