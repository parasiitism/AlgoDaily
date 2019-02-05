"""
    Questions to ask:
    - lower/upper case?
    - duplicate characters in t?
    - any space?
"""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str

        Time    O(n)
        Space   O(n)
        456 ms beats 6.27%
        """
        indexes = []
        minimum = s
        targetStructure = {}
        for c in t:
            if c in targetStructure:
                targetStructure[c] += 1
            else:
                targetStructure[c] = 1
        curStructure = {}
        for key in targetStructure:
            curStructure[key] = 0

        for i in range(len(s)):
            c = s[i]
            if c in targetStructure:
                indexes.append(i)
                curStructure[c] += 1
                # check recursively
                while self.checkSameStructure(targetStructure, curStructure):
                    end = indexes[-1]
                    start = indexes[0]
                    length = end-start+1
                    if length < len(minimum):
                        minimum = s[start:end+1]
                    popped = indexes.pop(0)
                    curStructure[s[popped]] -= 1
        if len(minimum) == len(s):
            cur = {}
            for key in targetStructure:
                cur[key] = 0
            for i in range(len(s)):
                c = s[i]
                if c in targetStructure:
                    cur[c] += 1
            if self.checkSameStructure(targetStructure, cur):
                return s
            else:
                return ""
        return minimum

    def checkSameStructure(self, a, b):
        for key in a:
            if key not in b:
                return False
            elif a[key] > b[key]:
                return False
        return True


print(Solution().minWindow("ADOBECODEBANC", "ABC"))
print(Solution().minWindow("ADOBECODEBANC", "ABCB"))
print(Solution().minWindow("ADOBECODEBANCBABB", "ABC"))
print(Solution().minWindow("ADOBBECCOBDEBANC", "ABC"))
print(Solution().minWindow("ADOBECODEBANC", "ABc"))
