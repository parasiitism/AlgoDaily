from math import *

"""
    1st: math, learned from others
    - idea.png

    Time    O(log(PQ)) <- gcd
    Space   O(1)
"""


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        product = p * q // gcd(p, q)
        rooms = product//p
        reflections = product//q
        if reflections % 2 == 0:
            return 2
        if rooms % 2 == 0:
            return 0
        return 1
