"""
    1st: hashtable
    - learned from others https://leetcode.com/problems/string-transforms-into-another-string/discuss/355382/JavaC%2B%2BPython-Need-One-Unused-Character
    - There are 2 possibilites to transform a string
        1. 1 to 1:
            e.g. abbc -> xyyx
        2. Many to 1:
            e.g. aabccc -> ccdeee
            We should do
                - c->e to make aabeee
                - b->d to make ccdeee
                - a->x to make xxdeee
                - x->c to make ccdeee
            In this way, since we use an extra character, we wont mess up the transformation from a->c directly
    - as we need an extra character, we need to check if s2 has it

    Time    O(N)
    Space   O(26)
    32 ms, faster than 55.31%
"""


class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        ht = {}
        n = len(str1)
        for i in range(n):
            c1 = str1[i]
            c2 = str2[i]
            if c1 in ht and ht[c1] != c2:
                return False
            ht[c1] = c2
        return len(set(str2)) < 26
