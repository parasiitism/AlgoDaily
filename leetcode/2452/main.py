"""
    string
    
    Time    O(QDN)
    Space   O(Q) the result
    262 ms, faster than 100.00%
"""


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        for q in queries:
            for w in dictionary:
                diff = 0
                for i in range(len(q)):
                    if q[i] != w[i]:
                        diff += 1
                if abs(diff) <= 2:
                    res.append(q)
                    break
        return res
