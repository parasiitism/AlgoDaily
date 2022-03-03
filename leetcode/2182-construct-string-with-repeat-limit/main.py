from heapq import *

"""
    1st: hashtable + maxheap
    - count the freq of each character
    - append the largest character(zyx...cba) to the result, and use some 2nd largest charactoers as a delimiter along the way
    - be careful that some suffux characters would be appended too often

    Time    O(Nlog26)
    Space   O(N)
    851 ms, faster than 75.00%
"""


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        d = 26 * [0]
        for c in s:
            i = ord(c) - ord('a')
            d[i] += 1
        maxheap = []
        for i in range(26):
            if d[i] > 0:
                heappush(maxheap, (-i, d[i]))

        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        res = ''
        cur = [-2**32, 0]
        while len(maxheap) > 0:

            prevLen = len(res)

            acidx, cnt = heappop(maxheap)
            toSubtract = 0
            if acidx == cur[0]:
                toSubtract = min(repeatLimit - cur[1], cnt)  # be careful
                cur = [acidx, toSubtract + cur[1]]  # be careful
            else:
                toSubtract = min(repeatLimit, cnt)
                cur = [acidx, toSubtract]

            res += toSubtract * alphabets[-acidx]
            cnt -= toSubtract

            if len(maxheap) > 0:
                acidx2, cnt2 = heappop(maxheap)
                res += alphabets[-acidx2]
                cnt2 -= 1
                cur = [acidx2, 1]
                if cnt2 > 0:
                    heappush(maxheap, (acidx2, cnt2))

            if cnt > 0:
                heappush(maxheap, (acidx, cnt))

            # stop the iteration if no more characters can be appended
            if len(res) == prevLen:
                break

        return res
