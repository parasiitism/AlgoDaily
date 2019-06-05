import heapq
from collections import *

"""
    1st approach: heap
    - similar to lc621
    1. count occurence for each task
    2. in each iteration
        - pop the tasks from maxheap n+1 times
        - put the tasks back to the queue with decremented count
    3. remove trailing '-'(idle)

    Time    O(nlogn)
    Space   O(n)
    1296 ms, faster than 13.14%
"""


import heapq
from collections import *


class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k <= 1:
            return s
        # count occurence for each task
        counter = Counter(s)
        pq = []
        for key in counter:
            heapq.heappush(pq, (-counter[key], key))
        res = ""
        while len(pq) > 0:
            arr = []
            # pop the tasks from maxheap
            for i in range(k):
                if len(pq) > 0:
                    pop = heapq.heappop(pq)
                    res += pop[1]
                    arr.append(pop)
                else:
                    res += "-"
            # put the tasks back to the queue with decremented count
            for count, key in arr:
                if abs(count) > 1:
                    heapq.heappush(pq, (count+1, key))
        while len(res) > 0:
            if res[-1] == '-':
                res = res[:-1]
            else:
                break
        if res.find("-") > -1:
            return ""
        # res is the list of tasks
        return res
