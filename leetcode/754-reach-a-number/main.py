"""
    1st: bfs

    Time    O(2^n)
    LTE
"""


class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        steps = 0
        total = 0
        while total < target:
            steps += 1
            total += steps
        while total - target % 2 != 0:
            steps += 1
            total += steps
        return steps


"""
    2nd: math

    honestly, i dont think i can come up with this during an interview, it requires a very detailed understanding from math perspective

    e.g. 7
    1 + 2 + 3 + 4 = 10 > 7
    (10 - 7) = 3 which is an odd so we keep going forward
    (15 - 7) = 8 which is an even we can stop now
    because 1 + 2 + 3 + 4 + 5 - 2(4) = 7

    e.g. 8
    1 + 2 + 3 + 4 = 10 > 8
    (10 - 8) = 2 which is an even we can stop now
    because 1 + 2 + 3 + 4 + 5 - 2(1) = 8

    e.g. 9
    1 + 2 + 3 + 4 = 10 > 9
    (10 - 9) = 1 which is an odd so we keep going forward
    (15 - 9) = 6 which is an even we can stop now
    because 1 + 2 + 3 + 4 + 5 - 2(3) = 9

    Time    O(sqrt(n))
    Space   O(1)
    80 ms, faster than 54.58%
"""


class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        steps = 0
        total = 0
        while total < target:
            steps += 1
            total += steps
        while (total - target) % 2 != 0:
            steps += 1
            total += steps
        return steps
