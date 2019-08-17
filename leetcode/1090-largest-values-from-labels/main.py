from collections import *
import heapq

"""
    1st approach: heap + hashtable
    - the question is poorly described, here is my understanding
    
    e.g.1
    values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1
    Label 1 -> [5,4]
    Label 2 -> [3,2]
    Label 3 -> [1]

    from label 1 : we take 5,
    from label 2: we take 3
    from label 3: we take 1 (since label 1 has only one element)
    result = 5+3+1=9

    e.g.2
    Input: values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit = 2
    Label 1 -> [5]
    Label 2 -> [1]
    Label 3 -> [4,3,2]

    from label 1: take 5
    from label 3: take 4,3 (at most 2, becos use_limit = 2)
    now we have 3 numbers, reach to the limit, num_wanted = 3, so we stop
    result = 5+4+3 = 12

    better question description:
    - https://leetcode.com/problems/largest-values-from-labels/discuss/313011/Question-Explanation-and-Simple-Solution-or-Java-or-100

    Time    O(nlogn)
    Space   O(n)
    156 ms, faster than 19.65%
"""


class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        pq = []
        ht = defaultdict(list)
        for i in range(len(values)):
            key = labels[i]
            val = values[i]
            ht[key].append(val)
            heapq.heappush(pq, (-val, key))
        seen = defaultdict(int)
        count = 0
        res = 0
        while len(pq) > 0:
            pop, key = heapq.heappop(pq)
            if seen[key] == use_limit:
                continue
            seen[key] += 1
            res -= pop
            count += 1
            if count == num_wanted:
                break
        return res
