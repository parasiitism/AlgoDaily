"""
    line sweep

    Time    O(N)
    Space   O(N)
"""


class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        line_sweep = (n+1) * [0]
        for p, r in lights:
            left = max(0, p - r)
            right = min(n-1, p + r)
            line_sweep[left] += 1
            line_sweep[right+1] -= 1
        pfs = 0
        for i in range(n):
            pfs += line_sweep[i]
            line_sweep[i] = pfs
        res = 0
        for i in range(n):
            if line_sweep[i] >= requirement[i]:
                res += 1
        return res
