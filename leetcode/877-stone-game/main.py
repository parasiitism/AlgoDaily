"""
    1st: dynamic programming
    - if alice pick the A[i], she can always pick the A[i+2] or A[j] in her next round
    - if alice pick the A[j], she can always pick the A[i] or A[j-1] in her next round

    Time    O(N^2)
    Space   O(N^2)
    325 ms, faster than 47.02%
"""


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        ht = {}

        def f(i, j):
            if i >= j:
                return 0
            key = (i, j)
            if key in ht:
                return ht[key]
            a = piles[i] + f(i+2, j)
            b = piles[j] + f(i, j-2)
            ht[key] = max(a, b)
            return ht[key]

        alice = f(0, len(piles)-1)
        bob = sum(piles) - alice

        return alice > bob


"""
    2nd: logic
    - alice can always win, because she always has the options first AND there are even number of stones
"""


class Solution(object):
    def stoneGame(self, piles):
        return True


"""
    In real interviews, follow-ups would be:
    - the number of stones can be odd
    - the best score alice can get
"""
