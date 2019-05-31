class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]

        Time    O(SP)   iterate S, for each substring of length P, check if anagram 
        Space   O(2*P)
        168 ms, faster than 51.27%
        """
        m = {}
        for c in p:
            self.putHashtable(c, m)
        cur = {}
        window = s[:len(p)]
        for c in window:
            self.putHashtable(c, cur)
        res = []
        if self.samehashtable(m, cur) == True:
            res.append(0)
        for i in range(len(p), len(s)):
            earliest = s[i-len(p)]
            cur[earliest] -= 1
            if cur[earliest] == 0:
                del cur[earliest]
            self.putHashtable(s[i], cur)
            if self.samehashtable(m, cur) == True:
                res.append(i-len(p)+1)
        return res

    def putHashtable(self, c, ht):
        if c in ht:
            ht[c] += 1
        else:
            ht[c] = 1

    def samehashtable(self, a, b):
        for c in a:
            if c not in b:
                return False
            if c in b and a[c] != b[c]:
                return False
        return True


print(Solution().findAnagrams("cbaebabacd", "abc"))
print(Solution().findAnagrams("abab", "ab"))


"""
    2nd approach: sliding window
    - check if each substring is an anagram but dont use slice in every iteration

    Time    O(n*m)
    Space   O(m)
    204 ms, faster than 32.10%
"""


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_structure = 26 * [0]
        cur_structure = 26 * [0]
        for c in p:
            p_structure[ord(c) - ord('a')] += 1
        # iterate
        res = []
        for i in range(len(s)):
            # substract last character from window after i == len(p)
            if i >= len(p):
                earliest = s[i - len(p)]
                cur_structure[ord(earliest) - ord('a')] -= 1
            # add character to the window
            cur_structure[ord(s[i]) - ord('a')] += 1
            # check structure
            if self.sameStructure(p_structure, cur_structure) == True:
                # append index of the earlierest character in this string
                res.append(i - len(p) + 1)
        return res

    def sameStructure(self, a, b):
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True


print(findAnagrams("cbaebabacd", "abc"))
print(findAnagrams("abab", "ab"))
