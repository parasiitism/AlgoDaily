""" 
    2nd approach: 2 hashtables
    - 1st hashtable for str1[i] -> str2[i]
    - 2nd hashtable for str2[i] -> str1[i]

    Time  O(n)
    Space O(n)
    24 ms, faster than 99.62%
"""


class Solution(object):
    def isIsomorphic(self, a, b):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        forward = {}
        backward = {}
        for i in range(len(a)):
            c1 = a[i]
            c2 = b[i]
            if c1 not in forward:
                forward[c1] = c2
            else:
                if forward[c1] != c2:
                    return False
            if c2 not in backward:
                backward[c2] = c1
            else:
                if backward[c2] != c1:
                    return False
        return True
