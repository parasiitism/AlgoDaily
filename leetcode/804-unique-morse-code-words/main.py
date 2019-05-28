"""
    1st approach: hashtable

    Time    O(nk) n: number of words, k: number of characters of each word
    Space   O(nk)
    24 ms, faster than 70.67%
"""


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        hs = set()
        for word in words:
            temp = ""
            for c in word:
                idx = ord(c) - ord('a')
                temp += morse[idx]
            hs.add(temp)
        return len(hs)
