
from heapq import *

"""
    1st: max heap
    - milestones can be huge, so LTE
    - THIS aapproach is incorret, consider [100,100,100], the result should be 300

    Time    O(NlogM)
    Space   O(N)
    WA
"""


class Solution:
    # one by one
    def numberOfWeeks(self, milestones: List[int]) -> int:
        pq = []
        for i in range(len(milestones)):
            heappush(pq, (-milestones[i], i))
        count = 0
        prev = None
        while len(pq) > 0:
            skipped = None
            if pq[0][1] == prev:
                skipped = heappop(pq)

            if len(pq) == 0:
                break

            freq, i = heappop(pq)
            _freq = -(-freq-1)
            count += 1
            if _freq != 0:
                heappush(pq, (_freq, i))
            prev = i

            if skipped:
                heappush(pq, skipped)
        return count
    # bulk by bulk

    def numberOfWeeks(self, milestones: List[int]) -> int:
        pq = []
        for i in range(len(milestones)):
            heappush(pq, (-milestones[i], i))
        count = 0
        while len(pq) >= 2:
            a, i = heappop(pq)
            b, j = heappop(pq)
            a, b = -a, -b
            toWork = min(a, b)
            count += toWork * 2
            a -= toWork
            b -= toWork
            if a > 0:
                heappush(pq, (-a, i))
            if b > 0:
                heappush(pq, (-b, j))
        if len(pq) > 0:
            count += 1
        return count


"""
    2n: math
    - learned from others
    - the intuition is:
        - We must be able to finish all the timestones, unless there is one task that has too many miletones(more milestones then all other projects combined)

    ref:
    - https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/discuss/1375390/Python-Solution-with-detailed-explanation-and-proof-and-common-failure-analysis
    - https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/discuss/1375479/O(n)

    Time    O(N)
    Space   O(1)
    728 ms, faster than 66.67%
"""


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total, largest = sum(milestones), max(milestones)
        if total - largest >= largest:
            return total
        return 2 * (total - largest) + 1
