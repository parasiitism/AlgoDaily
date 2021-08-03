"""
    1st: math
    - class approach to find all the divisors

    Time    O(sqrt of N)
    Spce    O(sqrt of N)
    48 ms, faster than 50.00%
"""


class Solution:
    def isThree(self, n: int) -> bool:
        hs = set()
        i = 1
        while i <= n:
            if n % i == 0:
                hs.add(i)
                hs.add(n//i)
            i += 1
        return len(hs) == 3
