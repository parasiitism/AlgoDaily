"""
    1st approach: string slicing

    Time    O(n)
    Space   O(n)
    20 ms, faster than 91.06%
"""


class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        for i in range(len(s)-1):
            temp = s[i:i+2]
            if temp == '++':
                res.append(s[:i] + '--' + s[i+2:])
        return res


"""
    2nd approach: string checking the character ar i and i+1

    Time    O(n)
    Space   O(n)
    16 ms, faster than 95.74%
"""


class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        for i in range(len(s)-1):
            if s[i] == '+' and s[i+1] == '+':
                res.append(s[:i] + '--' + s[i+2:])
        return res
