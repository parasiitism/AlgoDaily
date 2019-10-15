"""
    1st: math

    Time    O(n)
    Space   O(1)
    36 ms, faster than 36.24%
"""


class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        n = len(distance)
        forward = 0
        i = start
        while i != destination:
            forward += distance[i]
            i = (i + 1) % n
        backward = 0
        i = start
        while i != destination:
            i = (i - 1 + n) % n
            backward += distance[i]
        return min(forward, backward)
