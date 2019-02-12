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
