"""
    1st: string, brute force

    e.g.
    (247+3)8
    (247+38)
    
    2(47+3)8
    2(47+38)
    
    24(7+3)8
    24(7+38)

    Time    O(N^2)
    Space   O(N)
    57 ms, faster than 70.00%
"""


class Solution:
    def minimizeResult(self, expression: str) -> str:
        plusIdx = -1
        for i in range(len(expression)):
            if expression[i] == '+':
                plusIdx = i
                break
        A = expression[:plusIdx]
        B = expression[plusIdx+1:]
        A = self.split(A)[:-1]
        B = self.split(B)[1:]
        res = None
        smallest = 2**32
        for a1, a2 in A:
            for b1, b2 in B:
                e = a1 + '(' + a2 + '+' + b1 + ')' + b2
                _e = a1 + '*(' + a2 + '+' + b1 + ')*' + b2
                if a1 == '':
                    _e = '1' + _e
                if b2 == '':
                    _e = _e + '1'
                try:
                    x = int(eval(_e))
                    if x < smallest:
                        smallest = x
                        res = e
                except Exception as err:
                    pass

        return res

    def split(self, s):
        pairs = []
        for i in range(len(s)+1):
            a = s[:i]
            b = s[i:]
            pairs.append((a, b))
        return pairs
