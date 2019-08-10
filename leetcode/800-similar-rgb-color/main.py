import sys

"""
    1st approach: math
    - tedious implementation

    Time    O(n)
    Space   O(n)
    40 ms, faster than 7.81%
"""


class Solution(object):
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """

        a = color[1:3]
        b = color[3:5]
        c = color[5:7]

        cands = ['00', '11', '22', '33', '44', '55', '66', '77',
                 '88', '99', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff']

        diff1 = sys.maxsize
        a_ = ''
        for cand in cands:
            temp = (self.hex2int(a) - self.hex2int(cand))**2
            if temp < diff1:
                diff1 = temp
                a_ = cand

        diff2 = sys.maxsize
        b_ = ''
        for cand in cands:
            temp = (self.hex2int(b) - self.hex2int(cand))**2
            if temp < diff2:
                diff2 = temp
                b_ = cand

        diff3 = sys.maxsize
        c_ = ''
        for cand in cands:
            temp = (self.hex2int(c) - self.hex2int(cand))**2
            if temp < diff3:
                diff3 = temp
                c_ = cand

        return '#' + a_ + b_ + c_

    def hex2int(self, hexi):
        res = 0
        m = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'a': 10,
            'b': 11,
            'c': 12,
            'd': 13,
            'e': 14,
            'f': 15,
        }
        for i in range(len(hexi)):
            res += m[hexi[i]] * 16**(len(hexi)-i-1)
        return res


"""
    2nd approach: math
    - same idea as 1st, but a bit more concise

    Time    O(n)
    Space   O(n)
    16 ms, faster than 89.06%
"""


class Solution(object):
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """

        a = color[1:3]
        b = color[3:5]
        c = color[5:7]

        a_ = self.getMinHex(a)
        b_ = self.getMinHex(b)
        c_ = self.getMinHex(c)

        return '#' + a_ + b_ + c_

    def getMinHex(self, x):

        cands = ['00', '11', '22', '33', '44', '55', '66', '77',
                 '88', '99', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff']

        diff = sys.maxsize
        x_ = ''
        for cand in cands:
            temp = (int(x, 16) - int(cand, 16))**2
            if temp < diff:
                diff = temp
                x_ = cand
        return x_
