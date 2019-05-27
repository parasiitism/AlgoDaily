"""
    1st approach: string splitting
    - split the string
    - reverse each word and put it to the result

    Time    O(nk)
    Space   O(n)
    24ms beats 83.33%
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        arr = []
        for word in words:
            arr.append(word[::-1])
        return ' '.join(arr)
