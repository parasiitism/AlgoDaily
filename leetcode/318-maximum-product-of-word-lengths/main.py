"""
    1st approach: brute-force with hashtable
    - count characters occurence of each word
    - naively iterate all the pairs in O(n^2) to find the pair in which both words have no common chars

    Time    O(26 n^2)
    Space   O(n)
    2308 ms, faster than 5.10%
"""


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        signatures = []
        for w in words:
            temp = 26 * [0]
            for c in w:
                temp[ord(c)-ord('a')] += 1
            signatures.append(temp)
        res = 0
        for i in range(len(signatures)-1):
            for j in range(i+1, len(signatures)):
                a = signatures[i]
                b = signatures[j]
                if self.checkHasCommon(a, b) == False:
                    res = max(res, len(words[i])*len(words[j]))
        return res

    def checkHasCommon(self, a, b):
        for i in range(26):
            if a[i] > 0 and b[i] > 0:
                return True
        return False


"""
    2nd approach: optimize the above approach by saving the characters with bit op
    - there are only 26 characters, and one number can be up to 32 bits. so, actually we can save each word in a number
        e.g. abdf -> 101011
                     ^ ^ ^^
                     f d ba
    - if we AND 2 numbers to see whether there is a common bit, 
        e.g.1 1011 & 0100 = 0, no common
        e.g.2 1011 & 0110 = 10, yes there is a common bit
    - naively iterate all the pairs in O(n^2) to find the pair in which both words have no common chars

    Time    O(n^2)
    Space   O(n)
    412 ms, faster than 56.69%
"""


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        signatures = []
        for w in words:
            temp = 0
            for c in w:
                # temp |= 1 << ord(c)-ord('a')
                temp = temp | (1 << ord(c)-ord('a'))
            signatures.append(temp)
        res = 0
        for i in range(len(signatures)-1):
            for j in range(i+1, len(signatures)):
                a = signatures[i]
                b = signatures[j]
                if a & b == 0:
                    res = max(res, len(words[i])*len(words[j]))
        return res
