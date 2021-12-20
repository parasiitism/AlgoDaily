"""
    1st: hashtable
    
    Time    O(M+N) M: string, N: spaces
    Space   O(M+N) include the result
    764 ms, faster than 100.00%
"""


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ''
        spacesSet = set(spaces)
        for i in range(len(s)):
            if i in spacesSet:
                res += ' '
            res += s[i]
        return res


"""
    2nd: 2 pointers

    Time    O(M)
    Space   O(M)
    764 ms, faster than 100.00%
"""


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ''
        j = 0
        for i in range(len(s)):
            if j < len(spaces) and i == spaces[j]:
                res += ' '
                j += 1
            res += s[i]
        return res
