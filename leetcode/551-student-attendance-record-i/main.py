"""
    1st approach: counting
    - be careful that we regard a student is bad when 'L's are continuous

    Time    O(n)
    Space   O(1)
    16 ms, faster than 95.01%
"""


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        continuousL = 0
        for c in s:
            if c == 'A':
                a += 1
                if a > 1:
                    return False
                continuousL = 0
            elif c == 'L':
                continuousL += 1
                if continuousL > 2:
                    return False
            else:
                continuousL = 0
        return True
