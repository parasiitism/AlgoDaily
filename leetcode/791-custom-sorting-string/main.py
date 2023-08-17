from collections import *

"""
    1st approach: hashtable
    - count the occurence, N, of each character and put the count in a hashtable
    - for each c in S, if c is in the hashtable, append the N*"c" in the result string and remove c from the hashtbale
    - for the remaining characters in the hashtable, put them back to the result string

    Time    O(S+T)
    Space   O(T)
    20 ms, faster than 58.70%
"""


class Solution(object):
    def customSortString(self, order: str, s: str) -> str:
        # count the occurence, N, of each character and put the count in a hashtable
        ctr = Counter(s)
        # for each c in S, if c is in the hashtable,
        # append the N*"c" in the result string and remove c from the hashtbale
        res = []
        for i in range(len(order)):
            c = order[i]
            freq = ctr[c]
            res.append(freq * c)
            ctr[c] = 0
        # for the remaining characters in the hashtable, put them back to the result string
        for remain_key in ctr:
            freq = ctr[remain_key]
            res.append(freq * remain_key)
        return ''.join(res)


a = "kqep"
b = "pekeq"
print(Solution().customSortString(a, b))

a = "cba"
b = "abeabfcd"
print(Solution().customSortString(a, b))

"""
    followup: for the characters not in S, append them to the result string by insertion order

    Time    O(S+T)
    Space   O(T)
    12 ms, faster than 99.67%
"""


class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        # count the occurence, N, of each character and put the count in a hashtable
        m = OrderedDict()
        for c in T:
            if c not in m:
                m[c] = 1
            else:
                m[c] += 1
        # for each c in S, if c is in the hashtable,
        # append the N*"c" in the result string and remove c from the hashtbale
        res = ""
        for c in S:
            if c in m:
                res += m[c] * c
                del m[c]
        # for the remaining characters in the hashtable, put them back to the result string
        for key in m:
            res += m[key] * key

        return res


a = "kqep"
b = "pekeq"
print(Solution().customSortString(a, b))

a = "cba"
b = "abeabfcd"
print(Solution().customSortString(a, b))
