"""
    hashtable

    ref:
    - https://leetcode.com/problems/total-appeal-of-a-string/discuss/1996203/DP
    - idea.png

    Time    O(N)
    Space   O(N)
    167 ms, faster than 100.00%
"""


class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        ht = {}
        res = 0
        cnt = 0
        for i in range(n):
            c = s[i]
            if c in ht:
                cnt += i - ht[c]
            else:
                cnt += i + 1
            ht[c] = i
            res += cnt
        return res
