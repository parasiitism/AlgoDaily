"""
    1st: math
    - find the total remain, use it to find the average and the leftover
    - contruct the result array with average
    - belance the result array with the leftover

    Time    O(M+N)
    Space   O(N)
    1584 ms, faster than 100.00%
"""


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total = m + n
        sum_m = sum(rolls)
        sum_n = total * mean - sum_m
        avg, r = sum_n // n, sum_n % n
        if avg < 1 or avg > 6:
            return []
        res = n * [avg]
        i = 0
        while r > 0 and i < n:
            diff = min(r, 6 - res[i])
            res[i] += diff
            r -= diff
            i += 1
        if r > 0:
            return []
        return res
