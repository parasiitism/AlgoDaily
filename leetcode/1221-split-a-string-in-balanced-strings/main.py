class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        l_count, r_count = 0, 0
        res = 0
        for c in s:
            if c == 'L':
                l_count += 1
            elif c == 'R':
                r_count += 1
            if l_count == r_count:
                res += 1
                l_count, r_count = 0, 0
        return res
