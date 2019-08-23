"""
    1st approach: iteration

    Time    O(n)
    Space   O(n)
    16 ms, faster than 66.27% 
"""


class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        res = ''
        for c in address:
            if c == '.':
                res += '[.]'
            else:
                res += c
        return res


"""
    2nd approach: string replace

    Time    O(n)
    Space   O(n)
    28 ms, faster than 6.64%
"""


class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace('.', '[.]')
