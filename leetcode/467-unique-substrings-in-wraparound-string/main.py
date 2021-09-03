"""
    1st: brute force

    Time    O(N^2)
    LTE
"""


class Solution(object):
    def findSubstringInWraproundString(self, p):
        n = len(p)
        if n == 0:
            return 0
        res = set()
        # count = 1
        sub = p[0]
        res.add(sub)
        for i in range(1, n):
            c = p[i]
            idx0 = ord(sub[-1]) - ord('a')
            idx1 = ord(c) - ord('a')

            if (idx0 + 1) % 26 == idx1:
                # count += 1
                # res += count
                sub += c
            else:
                # count = 1
                # res += 1
                sub = c
            sfs = ''
            for j in range(len(sub)-1, -1, -1):
                sfs += sub[j]
                res.add(sfs)
        # print(res)
        return len(res)


"""
    2nd: dynamic programming
    - similar to lc940
    idea:
    - every charecter in P has a count of 1
    - if prev+1 == cur, it means we can extend the length of the current temporary string, so we increase the ht[cur] by 1
    - the result is the sum of all count

    Time    O(N)
    Space   O(26)
    130 ms, faster than 17.55%
"""


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        res = {c: 1 for c in p}
        maxCount = 1
        for i in range(1, len(p)):
            c = p[i]
            curIdx = ord(p[i]) - ord('a')
            prevIdx = (ord(p[i-1]) - ord('a') + 1) % 26
            if curIdx == prevIdx:
                maxCount += 1
            else:
                maxCount = 1
            res[c] = max(res[c], maxCount)
        return sum(res.values())
