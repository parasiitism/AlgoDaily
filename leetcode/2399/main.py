"""
    hashtable

    Time    O(N)
    Space   O(N)
    97 ms, faster than 11.76%
"""


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        ht = defaultdict(list)
        for i in range(len(s)):
            c = s[i]
            ht[c].append(i)
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(len(distance)):
            d = distance[i]
            c = alphabets[i]
            if c in ht and len(ht[c]) == 2:
                indices = ht[c]
                if indices[1] - indices[0] - 1 != d:
                    return False
        return True
