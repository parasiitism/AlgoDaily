
from collections import deque
from bisect import *
"""
    1st: binary search
    - put every zero into a sorted list
    - for every one, binary search the left most zero index and count it

    Time    O(NlogN) -> O(N^2)
    Space   O(N)
    3455 ms, faster than 100.00% for now
"""


class Solution(object):
    def catchAllPeople(self, team, dist):
        n = len(team)
        zeros = []
        for i in range(n):
            if team[i] == 0:
                zeros.append(i)
        res = 0
        for i in range(n):
            if team[i] == 0:
                continue
            j = bisect_left(zeros, i-dist)
            if 0 <= j < len(zeros) and i-dist <= zeros[j] <= i+dist:
                res += 1
                zeros.pop(j)
        return res


"""
    2nd: queue
    - put every zero into a sorted list
    - for every one, count the left most legit index of zero, and discard it

    Time    O(N)
    Space   O(N)
    1040 ms, faster than 100.00%
"""


class Solution:
    def catchAllPeople(self, team: List[int], dist: int) -> int:
        n = len(team)
        zeros = deque()
        for i in range(n):
            if team[i] == 0:
                zeros.append(i)
        res = 0
        for i in range(n):
            if team[i] == 0:
                continue
            while len(zeros) > 0 and zeros[0] < i-dist:
                zeros.popleft()
            if len(zeros) > 0 and zeros[0] <= i+dist:
                zeros.popleft()
                res += 1
        return res
