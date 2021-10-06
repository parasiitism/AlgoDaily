from collections import *

"""
    1st: queue
    - put all the indices of X into a queue
    - count the 3-consecutive indices

    Time    O(2N)
    Space   O(N)
    36 ms, faster than 57.14%
"""


class Solution:
    def minimumMoves(self, s: str) -> int:
        q = deque()
        for i in range(len(s)):
            if s[i] == 'X':
                q.append(i)
        if len(q) == 0:
            return 0
        res = 0
        head = q.popleft()
        while len(q) > 0:
            pop = q.popleft()
            if pop >= head+3:
                res += 1
                head = pop
        return res + 1


"""
    2nd: array
    - optimize the storage usage of 1st approach

    Time    O(N)
    Space   O(N)
    36 ms, faster than 57.14%
"""


class Solution:
    def minimumMoves(self, s: str) -> int:
        res = 0
        head = None
        for i in range(len(s)):
            c = s[i]
            if c == 'X':
                if head == None:
                    head = i
                if i >= head+3:
                    res += 1
                    head = i
        if head == None:
            return res
        return res + 1
