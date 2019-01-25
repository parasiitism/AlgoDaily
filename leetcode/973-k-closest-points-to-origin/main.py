import heapq


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]


        2nd approach
        - calculate all the points distance
            - and put the items into a heap
        - the result is the first k items
        - the purpose of using .py is to get familar with 
        Time    O(nlogn)
        Space   O(n)
        548ms beats 98.95%
        25jan2019
        """
        heap = []
        for i, point in enumerate(points):
            dis = point[0]*point[0] + point[1]*point[1]
            heapq.heappush(heap, (dis, i))
        res = []
        for i in range(K):
            if i < len(points):
                idx = heapq.heappop(heap)[1]
                res.append(points[idx])
        return res


print(Solution().kClosest([[1, 3], [-2, 2]], 1))
print(Solution().kClosest([[1, 3], [-2, 2]], 3))
print(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2))
