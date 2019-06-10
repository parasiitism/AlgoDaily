"""
    1st approach: math
    - to get the result, just get the square root and iterate to the left to see if we have a * b = num

    Time    O(sqrt(area))
    Space   O(1)
    16 ms, faster than 96.03%
"""


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        root = math.sqrt(area)
        for i in range(int(root), 0, -1):
            remain = area / float(i)
            if remain.is_integer():
                r = int(remain)
                if i > remain:
                    return [i, r]
                else:
                    return [r, i]
        # dont need to return here because 1 must be able to divide all the numbers
