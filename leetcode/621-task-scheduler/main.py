import heapq
from collections import *

"""
    1st approach: maxheap
    1. count occurence for each task
    2. in each iteration
        - pop the tasks from maxheap n+1 times
        - put the tasks back to the queue with decremented count
    3. remove trailing '-'(idle)

    Time    O(nlogn)
    Space   O(n)
    744 ms, faster than 26.51%
"""


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # count occurence for each task
        counter = Counter(tasks)
        pq = []
        for key in counter:
            heapq.heappush(pq, (-counter[key], key))
        res = []
        while len(pq) > 0:
            arr = []
            # pop the tasks from maxheap
            for i in range(n+1):
                if len(pq) > 0:
                    pop = heapq.heappop(pq)
                    res.append(pop[1])
                    arr.append(pop)
                else:
                    res.append("-")
            # put the tasks back to the queue with decremented count
            for count, key in arr:
                if abs(count) > 1:
                    heapq.heappush(pq, (count+1, key))
        # remove trailing '-'(idle)
        while len(res) > 0:
            if res[-1] == '-':
                res.pop()
            else:
                break
        # res is the list of tasks
        return len(res)


print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2))
print(Solution().leastInterval(["A", "A", "A", "B", "B", "B", "C", "C"], 2))
print(Solution().leastInterval(
    ["A", "A", "A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D"], 2))
