from collections import *

"""
    1st: hashtable, math
    - keep in mind that every words[i] == 2, so there are 2 types of strings, we call them AB and AA
    - use a counter to count the longest strings from AB we can add on both sides to the result string
    - for the remaining AA strings
        - find the longest odd length
        - transform other odds to evens
        - sum up all the evens

    Time    O(N)
    Space   O(N)
    1500 ms, faster than 50.00%
"""


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        wordsCounter = Counter(words)
        bothSides = 0
        middleCandidates = Counter()
        for w in words:
            if w[0] == w[1]:
                middleCandidates[w] += 1
            else:
                _w = w[::-1]
                if _w in wordsCounter and wordsCounter[w] > 0 and wordsCounter[_w] > 0:
                    wordsCounter[w] -= 1
                    wordsCounter[_w] -= 1
                    bothSides += 4
        longestOddKey = ''
        longestOddMiddle = 0
        for key in middleCandidates:
            L = middleCandidates[key]
            if L % 2 == 1:
                if L > longestOddMiddle:
                    longestOddKey = key
                    longestOddMiddle = L
        evenBothSides = 0
        for key in middleCandidates:
            if key == longestOddKey:
                continue
            L = middleCandidates[key]
            L = L//2 * 2
            evenBothSides += L * 2
        return bothSides + longestOddMiddle * 2 + evenBothSides
