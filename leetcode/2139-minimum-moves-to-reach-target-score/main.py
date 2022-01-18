"""
    1st: math
    - reverse thinking, how to make to input back to 1

    Time    O(min(D, logN)) D=maxDoubles
    Space   O(1)
    51 ms, faster than 100.00%
"""


class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while target > 1:
            if maxDoubles > 0:
                if target % 2 == 0:
                    maxDoubles -= 1
                    target //= 2
                    res += 1
                else:
                    target -= 1
                    res += 1
            else:
                res += target - 1
                target = 1
        return res
