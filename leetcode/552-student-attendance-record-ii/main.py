"""
    1st: dynamic programming (recursion + hashtable)
    
    Time    O(6N)
    Space   O(6N)
    MLE
"""


class Solution:
    def checkRecord(self, N: int) -> int:
        ht = {}

        def f(n, A, L):
            if A >= 2:
                return 0
            if L >= 3:
                return 0
            if n == 0:
                return 1
            key = (n, A, L)
            if key in ht:
                return ht[key]
            p = f(n-1, A, 0)
            a = f(n-1, A+1, 0)
            l = f(n-1, A, L+1)
            ht[key] = (p + a + l) % (10**9 + 7)
            return ht[key]
        return f(N, 0, 0)


"""
    2nd: use LRU cache to minimize the memory usage
    - same idea as above

    Time    O(6N)
    Space   O(100)
    9415 ms, faster than 5.01%
"""


class Solution:
    def checkRecord(self, n: int) -> int:
        @lru_cache(100)  # the trick
        def f(i, absent, late):
            if i == 0:
                return 1
            # present, so no more consecutive late
            res = f(i-1, absent, 0)
            # absent, so no more consecutive late
            if absent < 1:
                res += f(i-1, absent+1, 0)
            # late
            if late < 2:
                res += f(i-1, absent, late+1)

            return res % (10**9+7)
