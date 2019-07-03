"""
    3rd approach: sliding window
    - similar to lc438

    Time    O(AB)
    Space   O(52)
    100 ms, faster than 21.89%
"""


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        p_structure = 26 * [0]
        cur_structure = 26 * [0]
        for c in s1:
            p_structure[ord(c) - ord('a')] += 1
        # iterate
        res = []
        for i in range(len(s2)):
            # substract last character from window after i == len(p)
            if i >= len(s1):
                leftmost = s2[i - len(s1)]
                cur_structure[ord(leftmost) - ord('a')] -= 1
            # add character to the window
            cur_structure[ord(s2[i]) - ord('a')] += 1
            # check structure
            if self.sameStructure(p_structure, cur_structure):
                # append index of the earlierest character in this string
                return True
        return False

    def sameStructure(self, a, b):
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True
