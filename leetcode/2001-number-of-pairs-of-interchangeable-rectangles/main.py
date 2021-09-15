from collections import *

"""
    1st: hashtable + math
    - use hashtable to count the number of w/h
    - use gcd to store the ratio of w/h instead of using floating numbers, to avoid precesion problem

    Time    O(Nlog(max(A, B)) + N)
    Space   O(N)
    3707 ms, faster than 16.67% 
"""


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ht = Counter()
        for w, h in rectangles:
            gcd = self.getGCD(w, h)
            w //= gcd
            h //= gcd
            ht[(w, h)] += 1
        res = 0
        for key in ht:
            x = ht[key] - 1
            res += (1+x) * x // 2
        return res

    def getGCD(self, a, b):
        if b == 0:
            return a
        return self.getGCD(b, a % b)


"""
    2nd: better math in one pass

    Time    O(Nlog(max(A, B)))
    Space   O(N)
    2020 ms, faster than 83.33%
"""


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ht = Counter()
        res = 0
        for w, h in rectangles:
            gcd = self.getGCD(w, h)
            w //= gcd
            h //= gcd
            res += ht[(w, h)]
            ht[(w, h)] += 1
        return res

    def getGCD(self, a, b):
        if b == 0:
            return a
        return self.getGCD(b, a % b)
