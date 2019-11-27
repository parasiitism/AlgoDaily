"""
    1st: array iteration
    - convert input N to a string
    - reverse the string and check if the outcome == input N

    Time    O(N)
    Space   O(N)
    20 ms, faster than 37.75% 
"""
class Solution(object):
    def confusingNumber(self, N):
        """
        :type N: int
        :rtype: bool
        """
        ht = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }
        res = ''
        s = str(N)
        for i in range(len(s)-1,-1,-1):
            c = s[i]
            if c not in ht:
                return False
            res += ht[c]
        return int(res) != N