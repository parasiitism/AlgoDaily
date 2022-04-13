"""
    1st: sort

    Time    O(NlogN) N: length of th input number
    Space   O(N)
    40 ms, faster than 60.00%
"""


class Solution:
    def largestInteger(self, num: int) -> int:
        s = str(num)
        digits = [int(c) for c in s]
        n = len(digits)
        oddIndices = set()
        odds = []
        evenIndices = set()
        evens = []
        for i in range(n):
            d = digits[i]
            if d % 2 == 0:
                evens.append(d)
                evenIndices.add(i)
            else:
                odds.append(d)
                oddIndices.add(i)
        odds.sort(key=lambda x: -x)
        evens.sort(key=lambda x: -x)
        res = []
        for i in range(n):
            if i in oddIndices:
                res.append(odds.pop(0))
            else:
                res.append(evens.pop(0))
        return ''.join([str(x) for x in res])
