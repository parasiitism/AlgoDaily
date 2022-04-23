from collections import *

"""
    1st: math

    If freq = 1, not possible, return -1
    If freq = 2, needs one 2-tasks
    If freq = 3, needs one 3-tasks
    If freq = 3k, freq = 3 * k, needs k batchs.
    If freq = 3k + 1, freq = 3 * (k - 1) + 2 + 2, needs k + 1 batchs
    If freq = 3k + 2, freq = 3 * k + 2, needs k + 1 batchs

    Time    O(N)
    Space   O(N)
    1320 ms, faster than 11.08% 
"""


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        # 30 30 30 10
        # 30 30 20 20
        ctr = Counter(tasks)
        res = 0
        for key in ctr:
            cnt = ctr[key]
            if cnt < 2:
                return -1
            elif cnt % 3 == 0:
                res += cnt//3
            else:
                res += cnt//3 + 1
        return res
