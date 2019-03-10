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
        548ms beats 13.23%
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


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]


        2nd approach: use builtin timsort

        Time    O(nlogn)
        Space   O(n)
        396 ms, faster than 69.73%
        10mar2019
        """
        arr = []
        for point in points:
            d2 = point[0]*point[0] + point[1]*point[1]
            arr.append((d2, point))
        arr = sorted(arr, key=lambda x: x[0])
        res = []
        for i in range(K):
            if i < len(arr):
                res.append(arr[i][1])
        return res


print(Solution().kClosest([[1, 3], [-2, 2]], 1))
print(Solution().kClosest([[1, 3], [-2, 2]], 3))
print(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2))
