"""
1st: dynamic programming
- bottom up recursion + hashtable
- generate all the possibilities by recursion
- cache the array of temporary result of number on each layer, ie. (num, N) to avoid redundant calculation

Time    less than O(2^N)
Space   less than O(2^N)
40 ms, faster than 71.91%
"""


class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        self.ht = {}
        res = set()
        start = 0 if N == 1 else 1
        for i in range(start, 10):
            temp = self.dfs(N, K, i)
            for x in temp:
                res.add(int(x))
        return list(res)

    def dfs(self, N, K, num):
        if num < 0 or num > 9:
            return []
        if N == 1:
            return [str(num)]

        if (num, N) in self.ht:
            return self.ht[(num, N)]

        left = self.dfs(N-1, K, num-K)
        right = self.dfs(N-1, K, num+K)

        res = []
        for x in left:
            res.append(str(num) + x)
        for y in right:
            res.append(str(num) + y)
        self.ht[(num, N)] = res
        return res


s = Solution()
a = 3
b = 7
print(s.numsSameConsecDiff(a, b))

a = 2
b = 1
print(s.numsSameConsecDiff(a, b))

a = 4
b = 2
print(s.numsSameConsecDiff(a, b))

a = 1
b = 0
print(s.numsSameConsecDiff(a, b))

a = 3
b = 0
print(s.numsSameConsecDiff(a, b))
