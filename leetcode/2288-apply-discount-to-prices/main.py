"""
    annoying string operation

    Time    O(N)
    Space   O(N)
    444 ms, faster than 33.33%
"""


class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split()
        res = []
        for w in words:
            cand = w[1:]
            if self.is_dollar_prefixed(w) and cand.isdigit():
                price = int(cand)
                temp = price - price * discount / 100.0
                res.append("${:.2f}".format(temp))
            else:
                res.append(w)
        return ' '.join(res)

    def is_dollar_prefixed(self, s):
        ctr = defaultdict(list)
        for i in range(len(s)):
            c = s[i]
            ctr[c].append(i)
        dollars = ctr['$']
        if len(dollars) != 1:
            return False
        return dollars[0] == 0
