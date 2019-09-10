"""
    1st: brute force O(n^2)
    - list out all the possibilities, e.g. 00000, 00001, 00011, 00111, 01111, 11111
    for each possibility, count the flips
    
    2nd: dynamic programming O(n)
    - as always, its a dynamic programming question, i didnt figure it out, i learned from the post
    
    https://leetcode.com/problems/flip-string-to-monotone-increasing/discuss/183896/Prefix-Suffix-Java-O(N)-One-Pass-Solution-Space-O(1)

    Time O(n)
    Space O(1)
    44 ms, faster than 91.64%
"""


class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        zeroCountAfterOne = 0
        oneCount = 0
        for i in range(len(S)):
            if S[i] == '0':
                if oneCount == 0:
                    continue
                zeroCountAfterOne += 1
            else:
                oneCount += 1
            if zeroCountAfterOne > oneCount:
                zeroCountAfterOne = oneCount
        return zeroCountAfterOne
