from heapq import *

"""
    1st: 2 maxheaps
    - store the length of consecutive As or Bs
    - shrink them 1 by 1 until we cannot do it anymore 

    Time    O(NlogN)
    Space   O(N)
    280 ms, faster than 42.86%
"""


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)

        maxheapA = []
        maxheapB = []

        c = colors[0]
        cnt = 1
        for i in range(1, n):
            if colors[i] == c:
                cnt += 1
            else:
                if c == 'A':
                    heappush(maxheapA, -cnt)
                else:
                    heappush(maxheapB, -cnt)
                c = colors[i]
                cnt = 1
        if c == 'A':
            heappush(maxheapA, -cnt)
        else:
            heappush(maxheapB, -cnt)

        turnIdx = 0  # even: alice; odd: bob
        while len(maxheapA) > 0 or len(maxheapB) > 0:
            if turnIdx % 2 == 0:
                if len(maxheapA) == 0 or -maxheapA[0] <= 2:
                    return False  # bob wins
                cnt = -heappop(maxheapA)
                cnt -= 1
                heappush(maxheapA, -cnt)
            else:
                if len(maxheapB) == 0 or -maxheapB[0] <= 2:
                    return True  # alice wins
                cnt = -heappop(maxheapB)
                cnt -= 1
                heappush(maxheapB, -cnt)
            turnIdx += 1


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = 0
        bob = 0
        for i in range(1, len(colors)-1):
            if colors[i-1] == colors[i] and colors[i] == colors[i+1]:
                if colors[i] == 'A':
                    alice += 1
                else:
                    bob += 1
        return alice > bob
