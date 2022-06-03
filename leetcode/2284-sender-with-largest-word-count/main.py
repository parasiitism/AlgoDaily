from collections import *

"""
    hashtable

    Time    O(N)
    Space   O(N)
    926 ms, faster than 40.00%
"""


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        ctr = Counter()
        n = len(senders)
        for i in range(n):
            msg = messages[i]
            sdr = senders[i]
            words = msg.split()
            count = len(words)
            ctr[sdr] += count
        res = ''
        res_cnt = 0
        for name in ctr:
            cnt = ctr[name]
            if cnt > res_cnt:
                res = name
                res_cnt = cnt
            elif cnt == res_cnt and name > res:
                res = name
        return res
