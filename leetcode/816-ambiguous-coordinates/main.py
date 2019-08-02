"""
    1st approach: a lot of if cases
    - add ',' in between the substrings
    - add '.' in between each substring, there are 4 cases
        - if '0', return [0]
        - if '0123', return [0.123] <- leading zeros
        - if '01230', return []     <- leading & tailing zeros
        - if '1230', return [1230]  <- only tailing zeros
    
    Time    O(n^3)
    Space   O(n)
    36 ms, faster than 85.05%
"""


class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        S = S[1:-1]
        arr = []
        for i in range(len(S)-1):
            temp = S[:i+1] + ',' + S[i+1:]
            arr.append(temp)
        res = []
        for s in arr:
            a, b = s.split(',')
            A = self.addDot(a)
            B = self.addDot(b)
            for x in A:
                for y in B:
                    res.append('(' + x + ', ' + y + ')')
        return res

    def addDot(self, s):
        if s[0] == '0':
            if len(s) == 1:
                return ['0']
            elif s[-1] != '0':
                return ['0.' + s[1:]]
            else:
                return []
        if s[-1] == '0':
            return [s]
        arr = [s]
        for i in range(len(s)-1):
            temp = s[:i+1] + '.' + s[i+1:]
            if int(s[i+1:]) != 0:
                arr.append(temp)
        return arr
