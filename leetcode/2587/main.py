"""
    greedy
    
    Time    O(2N + NlogN + N)
    Space   O(N)
"""


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        # split into positive and negative
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x <= 0]
        # start calculating prefix sum
        res = len(pos)
        pos_sum = 0
        if res > 0:
            pos_sum = sum(pos)
        # sum the negative numbers until prefix sum <= 0
        neg.sort(key=lambda x: -x)
        while len(neg) > 0 and pos_sum + neg[0] > 0:
            left = neg.pop(0)
            pos_sum += left
            res += 1
        return res
