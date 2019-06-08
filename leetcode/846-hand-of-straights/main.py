import heapq

"""
    1st approach: min heap
    - put the numbers into a min heap
    - pop the heap and put the item into a "straight" array if the pop == straight[-1] + 1, else put the poped item into a dump array
    - if the straight array is of size W, put the dumps back to the heap

    Time    O(n logn logn)
    Space   O(n)
    428 ms, faster than 41.14%
"""


class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        pq = []
        for num in hand:
            heapq.heappush(pq, num)
        straights = []
        while len(pq) > 0:
            straight = []
            dumps = []
            while len(pq) > 0 and len(straight) < W:
                pop = heapq.heappop(pq)
                if len(straight) == 0 or pop == straight[-1] + 1:
                    straight.append(pop)
                else:
                    dumps.append(pop)
            straights.append(straight)
            if len(straight) < W:
                return []
            else:
                for dump in dumps:
                    heapq.heappush(pq, dump)
        return straights


a = [1, 2, 3, 6, 2, 3, 4, 7, 8]
b = 3
print(Solution().isNStraightHand(a, b))

a = [1, 2, 3, 6, 2, 3, 4, 7, 8, 9, 10, 11]
b = 3
print(Solution().isNStraightHand(a, b))

a = [1, 2, 3, 6, 2, 3, 4, 7, 8, 9, 10, 12]
b = 3
print(Solution().isNStraightHand(a, b))

a = [1, 2, 3, 4, 5]
b = 4
print(Solution().isNStraightHand(a, b))

a = [5, 1]
b = 2
print(Solution().isNStraightHand(a, b))
