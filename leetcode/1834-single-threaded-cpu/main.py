from heapq import *

"""
    1st: sort + min heap
"""


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sortedTasks = []
        n = len(tasks)

        for i in range(n):
            eqT, procT = tasks[i]
            sortedTasks.append((eqT, procT, i))
        sortedTasks.sort()

        i = 0
        t = sortedTasks[0][0]
        minheap = []  # (processing_time, original_index)
        res = []
        while len(res) < n:
            while i < n and sortedTasks[i][0] <= t:
                heappush(minheap, (sortedTasks[i][1], sortedTasks[i][2]))
                i += 1
            if len(minheap) > 0:
                procT, idx = heappop(minheap)
                t += procT
                res.append(idx)
            elif i < n:
                t = sortedTasks[i][0]
        return res
