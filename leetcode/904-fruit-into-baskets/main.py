"""
    768 ms, faster than 20.82%
"""


class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        res = 0
        left = 0
        ht = {}
        for i in range(len(tree)):
            fruit = tree[i]
            if fruit not in ht:
                ht[fruit] = 1
            else:
                ht[fruit] += 1
            while len(ht) > 2:
                last = left
                left += 1
                leftMostFruit = tree[last]
                ht[leftMostFruit] -= 1
                if ht[leftMostFruit] == 0:
                    del ht[leftMostFruit]
            res = max(res, i-left+1)
        return res
