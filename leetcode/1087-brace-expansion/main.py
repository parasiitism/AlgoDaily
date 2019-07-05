"""
    1st approach: recursion
    - similar to lc17
    - basically explore all possiblities
    - actually the question is not good enough, consider {ab,bc}d

    Time    O(n^m) for the worst case because for each bracket, there might be m possibilities
    Space   O(n)
    20 ms, faster than 95.53%
"""


class Solution(object):
    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        chars = []
        for c in S:
            chars.append(c)

        m = {}
        s = ""
        while len(chars) > 0:
            pop = chars.pop(0)
            if pop == '{':
                tempList = self.parseOptions(chars)
                key = str(len(m))
                m[key] = tempList
                s += key
            else:
                s += pop
        self.res = []
        self.dfs(s, "", m)
        return self.res

    def parseOptions(self, chars):
        arr = []
        cur = ""
        while len(chars) > 0 and chars[0] != '}':
            pop = chars.pop(0)
            if pop == ',':
                arr.append(cur)
                cur = ""
            else:
                cur += pop
        arr.append(cur)
        chars.pop(0)
        return sorted(arr)

    def dfs(self, s, path, m):
        if len(s) == 0:
            self.res.append(path)
            return
        first = s[0]
        if first in m:
            for key in m[first]:
                self.dfs(s[1:], path+key, m)
        else:
            self.dfs(s[1:], path+first, m)


a = "{a,b}cf{d,e}"
print(Solution().expand(a))
