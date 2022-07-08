"""
    sort

    Time    O(NlogN)
    Space   O(N)
    1792 ms, faster than 8.18%
"""


class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort()
        workers.sort()
        res = 0
        for i in range(len(jobs)):
            j = jobs[i]
            w = workers[i]

            r = math.ceil(j / w)
            res = max(res, r)
        return res
