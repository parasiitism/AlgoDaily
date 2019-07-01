"""
    1st approach:
    - for k characters in 'even' group, reverse them and put them in to the result
    - for k characters in 'odd' group, just put them in to the result

    e.g.

    s = "abcdefghijk", k = 3
    
    0     1     2      3
    abc | def | ghi | jk
    ^           ^
    cba | def | ihg | jk

    Time    O(n)
    Space   O(n)
    56 ms, faster than 9.00%
"""


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ''
        cur = ''
        for i in range(len(s)):
            if (i//k) % 2 == 0:
                cur = s[i] + cur
            else:
                if len(cur) > 0:
                    res += cur
                    cur = ''
                res += s[i]
        if len(cur) > 0:
            res += cur
        return res


"""
    usually they ask this instead of the above version
    s = abcdefgh, k = 3
    return cbafedgh

    explanation: cba|fed|gh
"""


class Solution(object):
    def reverseStr(self, s, k):
        res = ''
        buf = ''
        for i in range(len(s)):
            if i % k == 0:
                res += buf[::-1]
                buf = ''
            buf += s[i]
        return res + buf


a = "abcdefgh"
b = 3
print(Solution().reverseStr(a, b))
