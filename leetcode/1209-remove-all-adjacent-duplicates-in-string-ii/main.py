"""
    1st: recursion
    e.g. s = pbbcggttciiippooaais, k = 2
    start from  = pbbcggttciiippooaais
    recursion 1 = pcciis
    recursion 2 = ps

    Time    O(nm) m depends on how many k duplicate characters from the input
    Space   O(n)
    104 ms, faster than 29.91% 
"""


class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        arr = []
        for c in s:
            arr.append(c)
        temp = self.dfs(arr, k)
        return ''.join(temp)

    def dfs(self, arr, k):
        if len(arr) == 0:
            return []
        res = []
        i = 0
        trimmed = False
        while i < len(arr):
            c = arr[i]
            j = i
            while j+1 < len(arr) and arr[j+1] == c:
                j += 1
            count = (j - i + 1) % k
            if j - i + 1 > count:
                trimmed = True
            res += count * c
            i = j + 1
        print()
        return self.dfs(res, k) if trimmed else arr


s = Solution()

a = "abcd"
b = 2
print(s.removeDuplicates(a, b))

a = "aabbccdd"
b = 2
print(s.removeDuplicates(a, b))

a = "deeedbbcccbdaa"
b = 3
print(s.removeDuplicates(a, b))

a = "pbbcggttciiippooaais"
b = 2
print(s.removeDuplicates(a, b))
