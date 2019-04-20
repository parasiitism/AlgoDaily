import heapq

"""
    1st approach: heap + merge intervals
    1. put all the intervals into a heap
    2. merge the intervals
    3. the result is exactly the time between the merged intervals

    Time    O(nlogn) n: number of intervals
    Space   O(n)
    204 ms, faster than 17.74% 
"""


class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[List[int]]]
        :rtype: List[List[int]]
        """
        pq = []
        for intvs in schedule:
            for intv in intvs:
                heapq.heappush(pq, (intv[0], intv[1]))
        if len(pq) == 0:
            return []
        start, end = heapq.heappop(pq)
        merged = [[start, end]]
        while len(pq) > 0:
            start, end = heapq.heappop(pq)
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        res = []
        for i in range(1, len(merged)):
            start = merged[i-1][1]
            end = merged[i][0]
            res.append([start, end])
        return res


a = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
print(Solution().employeeFreeTime(a))

a = [[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]
print(Solution().employeeFreeTime(a))
