"""
    math
    - sum of reward2 + k largest (reward1 - reward2)

    Time    O(NlogN)
    Space   O(N)
"""


from heapq import *


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        pairs = []
        for i in range(n):
            diff = reward1[i] - reward2[i]
            pairs.append(diff)
        pairs.sort(key=lambda x: -x)
        return sum(reward2) + sum(pairs[:k])


"""
    math + min heap
    - sum of reward2 + k largest (reward1 - reward2)

    Time    O(NlogK)
    Space   O(K)
"""


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        minheap = []
        for i in range(n):
            diff = reward1[i] - reward2[i]
            heappush(minheap, diff)
            if len(minheap) > k:
                heappop(minheap)
        return sum(reward2) + sum(minheap)
