"""
    1st approach: math
    - just do subtraction. borrow 'length' if we dont have enough 'quota'

    Time    O(n)
    Space   O(1)
    16 ms, faster than 86.50% 
"""


class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        length = 0
        quota = 100
        for c in S:
            idx = ord(c) - ord('a')
            if quota >= widths[idx]:
                quota -= widths[idx]
            else:
                length += 1
                quota = 100 - widths[idx]
        return [length+1, 100-quota]
