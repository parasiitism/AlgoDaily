import math

"""
    1st: lower bound binary search
    - learned from others
    - the basic idea is to find a speed that can Koko eat all bananas in H hours?
    - the bounds must be 1 < x < max(pile[i])

    ref:
    - https://blog.csdn.net/fuxuemingzhu/article/details/82716042
    - https://leetcode.com/problems/koko-eating-bananas/discuss/152324/C%2B%2BJavaPython-Binary-Search

    Time    O(nlogn)
    Space   O(1)
    664 ms, faster than 18.34%
"""


class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        minSpeed, maxSpeed = 1, max(piles)
        while minSpeed < maxSpeed:
            speed = (minSpeed + maxSpeed) // 2
            # find the total number of hours that
            # if we use the current  speed
            hour = 0
            for p in piles:
                hour += math.ceil(p / float(speed))
            # lower bound binary search
            if hour <= H:
                maxSpeed = speed
            else:
                minSpeed = speed + 1
        return minSpeed  # or maxSpeed
