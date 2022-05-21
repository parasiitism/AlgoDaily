"""
    hashtable

    Time    O(N)
    Space   O(N)
    78 ms, faster than 85.71%
"""


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []

        first = words[0]
        cur_key = self.count_chars(first)

        res.append(first)

        for i in range(1, len(words)):
            w = words[i]
            key = self.count_chars(w)
            if key == cur_key:
                continue
            cur_key = key
            res.append(w)
        return res

    def count_chars(self, s):
        ctr = 26 * [0]
        for c in s:
            idx = ord(c) - ord('a')
            ctr[idx] += 1
        return tuple(ctr)
