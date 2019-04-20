"""
    1st approach: 2 pointers
    1  1 pointer for arrayA, 2 pointer for arrB
    2. extract the overlapping time from A[p1] and B[p2]
    3. move forward the pointer in which the interval has minimum end time

    e.g.
    A = [[0,2],[5,10],[13,23],[24,25]]
    B = [[1,5],[8,12],[15,24],[25,26]]

    [0,2] and [1,5] => [1, 2]
    [5, 10] and [1, 5] => [5, 5]
    [5, 10] and [8, 12] => [8, 10]
    [13, 23] and [8, 12] => [13, 12] but start must be less than end so discard
    [13, 23] and [15, 24] => [15, 23]
    [24, 25] and [15, 24] => [24, 24]
    [24, 25] and [25, 26] => [25, 25]

    result = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

    Time    O(A+B)
    Space   O(n)
    132 ms, faster than 30.82%
    20apr2019
"""


class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """
        if len(A) == 0 or len(B) == 0:
            return []
        p1 = 0
        p2 = 0
        raw = []
        while p1 < len(A) and p2 < len(B):
            itvA = A[p1]
            itvB = B[p2]
            a = max(itvA[0], itvB[0])
            b = min(itvA[1], itvB[1])
            if a <= b:
                raw.append([a, b])
            if itvA[1] < itvB[1]:
                p1 += 1
            elif itvA[1] > itvB[1]:
                p2 += 1
            else:
                p1 += 1
                p2 += 1
        return merged
