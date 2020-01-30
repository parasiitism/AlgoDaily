"""
    1st: brain teaser, learned from others

    ther are 3 cases

    1.
    xx
    yy
    we can make them them same by 1 swap
    
    2.
    yy
    xx
    we can make them them same by 1 swap too

    3.
    xy
    yx
    we can make them them same by 2 swaps

    Consider the example 4
    s1 = "xxyyxyxyxx",
    s2 = "xyyxyxxxyx"

    First remove the indexes with same characters:
    s1 = "xyxyyx"
    s2 = "yxyxxy"

    "x_y" count = 3 (index 0, 2, 5)
    "y_x" count = 3 (index 1, 3, 4)

    index 0 and 2 can be made equal in just 1 swap. see case 1.
    index 1 and 3 can also be made equal in just 1 swap. see case 2.
    index 5 and 4 can be made Equal in 2 swaps. see case 3.

    so, at the end,  we only need 4 swaps.

    ref:
    - https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/discuss/419639/Python3-4-liner-w-explanation
    - https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/discuss/419874/Simply-Simple-Python-Solution-with-detailed-explanation

    Time    O(N)
    Space   O(1)
    28 ms, faster than 63.96%
"""


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy, yx = 0, 0
        for c1, c2 in zip(s1, s2):
            if c1 == 'x' and c2 == 'y':
                xy += 1
            elif c1 == 'y' and c2 == 'x':
                yx += 1
        # the sum of them must be even so that we can swap
        if (xy + yx) % 2 != 0:
            return -1
        # cases: (xx, yy) and (yy, xx), we need 1 swap for each
        res = xy // 2 + yx // 2
        # case: (xy, yx), we need 2 swaps
        if xy % 2 == 1:
            res += 2
        return res
