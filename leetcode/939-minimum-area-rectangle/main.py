import sys
from collections import *

"""
    1st approach: hashtable
    - reuse the way in lc750

    Time    O(RCC)
    Space   O(CC)
    TLE, it fails becos the numbers in coordinates are too big
"""


class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0 or len(points[0]) == 0:
            return 0

        maxR = 0
        for i, j in points:
            maxR = max(maxR, i+1)
        maxC = 0
        for i, j in points:
            maxC = max(maxC, j+1)

        matrix = []
        for _ in range(maxR):
            matrix.append(maxC*[0])

        for i, j in points:
            matrix[i][j] = 1

        res = sys.maxsize
        m = {}
        for i in range(maxR):
            for j in range(maxC):
                if matrix[i][j] == 1:
                    for k in range(j+1, maxC):
                        if matrix[i][k] == 1:
                            key = str(j) + ',' + str(k)
                            if key in m:
                                lastRow = m[key]
                                area = (k-j)*(i-lastRow)
                                res = min(res, area)
                            m[key] = i
        if res == sys.maxsize:
            return 0
        return res


"""
    2st approach: hashtable
    - actually the approach is similar to 1st but since the numbers in coordinates are too big
        , we need to use something else to store the coordinates instead of a 2D array
    - one possible way is first sort the intervals
    - then use an ordered dict to store them
    - then for every pair on a row, find out its cooresponding left and right(such that we can form a retangle) from the bottom

    Time    O(RRCC)
    Space   O(CC)
    2108 ms, faster than 24.04%
"""


class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0 or len(points[0]) == 0:
            return 0

        def cmpter(a, b):
            if a[0] == b[0]:
                return a[1]-b[1]
            return a[0]-b[0]

        points = sorted(points, cmp=cmpter)

        od = OrderedDict()
        for i, j in points:
            if i not in od:
                od[i] = set()
            od[i].add(j)

        res = sys.maxsize
        items = od.items()

        for key1, set1 in items:
            arr = list(set1)
            for left in arr:
                for right in arr:
                    if left == right:
                        continue
                    for key2, set2 in items:
                        if key1 == key2:
                            continue
                        bottomLeft = left in set2
                        bottomRight = right in set2
                        if bottomLeft and bottomRight:
                            area = abs((right-left)*(key2-key1))
                            res = min(res, area)

        if res == sys.maxsize:
            return 0
        return res


a = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
print(Solution().minAreaRect(a))

a = [[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]
print(Solution().minAreaRect(a))

print("-----")

"""
    3rd approach: hashtable. optimze the 2nd approach by only scan the rows in the bottom
    - actually the approach is similar to 1st but since the numbers in coordinates are too big
        , we need to use something else to store the coordinates instead of a 2D array
    - one possible way is first sort the intervals
    - then use an ordered dict to store them
    - then for every pair on a row, find out its cooresponding left and right(such that we can form a retangle) from the bottom

    Time    O(RRCC)
    Space   O(CC)
    740 ms, faster than 79.11%
"""


class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0 or len(points[0]) == 0:
            return 0

        def cmpter(a, b):
            if a[0] == b[0]:
                return a[1]-b[1]
            return a[0]-b[0]

        points = sorted(points, cmp=cmpter)

        od = OrderedDict()
        for i, j in points:
            if i not in od:
                od[i] = set()
            od[i].add(j)

        res = sys.maxsize
        items = od.items()

        for i in range(len(items)):
            key1 = items[i][0]
            set1 = items[i][1]
            arr = list(set1)
            for j in range(len(arr)):
                left = arr[j]
                for k in range(j+1, len(arr)):
                    right = arr[k]
                    for nextI in range(i+1, len(items)):
                        key2 = items[nextI][0]
                        set2 = items[nextI][1]
                        bottomLeft = left in set2
                        bottomRight = right in set2
                        if bottomLeft and bottomRight:
                            area = abs((right-left)*(key2-key1))
                            res = min(res, area)
                            break
        if res == sys.maxsize:
            return 0
        return res


a = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
print(Solution().minAreaRect(a))

a = [[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]
print(Solution().minAreaRect(a))
