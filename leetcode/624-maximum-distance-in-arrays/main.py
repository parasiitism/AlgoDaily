"""
    1st approach:
    - since we need to find the min/max from a different array, we need 2 variables to store the previous min and max
    
    e.g.               min max
    [
        [4,5],
        [1,2,3],        4   5
        [1,2,2],        1   5
        [-10,1],        1   5
    ]

    144 ms, faster than 38.16%
"""


class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        res = 0
        prevMin = arrays[0][0]
        prevMax = arrays[0][-1]
        for i in range(1, len(arrays)):
            arr = arrays[i]
            # use current min and max to compute the distance
            curMin = arr[0]
            curMax = arr[-1]
            # see if there is max distance
            a = abs(curMin-prevMax)
            b = abs(curMax-prevMin)
            res = max(res, a, b)
            # update previous min and max
            prevMin = min(prevMin, curMin)
            prevMax = max(prevMax, curMax)
        return res
