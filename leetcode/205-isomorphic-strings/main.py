""" 
    2nd approach: 2 hashtables
    - 1st hashtable for str1[i] -> str2[i]
    - 2nd hashtable for str2[i] -> str1[i]

    Time  O(n)
    Space O(n)
    48 ms, faster than 28.37%
"""


class Solution(object):
    def isIsomorphic(self, a, b):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ht_f = {}
        ht_b = {}
        for i in range(len(a)):
            c1 = a[i]
            c2 = b[i]
            if c1 in ht_f:
                if ht_f[c1] != c2:
                    return False
            if c2 in ht_b:
                if ht_b[c2] != c1:
                    return False
            else:
                ht_f[c1] = c2
                ht_b[c2] = c1
        return True
