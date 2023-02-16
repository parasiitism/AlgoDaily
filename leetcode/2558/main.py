from heapq import *

"""
    max heap

    Time    O(KlogN)
    Space   O(N)
"""
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        res = 0
        A = []
        for i in range(len(gifts)):
            x = gifts[i]
            heappush(A, (-x, i))
        while k > 0:
            max_a, idx = heappop(A)
            x = int(math.sqrt(-max_a))
            heappush(A, (-x, idx))
            k -= 1
        for x, i in A:
            gifts[i] = x
        return -sum(gifts)

