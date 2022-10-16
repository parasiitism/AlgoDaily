"""
    hashtable
    - pure string implementation without using any lib

    Time    O(1440 * 2)
    Space   O(4)
    153 ms, faster than 50.00%
"""


class Solution:
    def countTime(self, time: str) -> int:
        unknowns = set()
        for i in range(len(time)):
            d = time[i]
            if d == '?':
                unknowns.add(i)
        all_times = []
        for i in range(24):
            h = self.int2str(i)
            for j in range(60):
                m = self.int2str(j)
                all_times.append(h+':'+m)
        res = 0
        for t in all_times:
            digits = [c for c in t]
            for j in range(len(t)):
                if j in unknowns:
                    digits[j] = '?'
            temp = ''.join(digits)
            if temp == time:
                res += 1
        return res

    def int2str(self, i):
        s = ''
        if i < 10:
            s = '0'+str(i)
        else:
            s = str(i)
        return s
