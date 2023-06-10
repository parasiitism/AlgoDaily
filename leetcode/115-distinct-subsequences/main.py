"""
    1st: brute force
    - try all the possibilities to see if T can be formed

    Time    O(2^n)
    Space   O(2^n) recursion tree
    LTE
"""


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # self.ht = {}
        return self.dfs('', s, t)

    def dfs(self, a, s, t):
        if len(s) == 0:
            if a == t:
                return 1
            else:
                return 0
        # key = (a, s)
        # if key in self.ht:
        #     return self.ht[key]
        count = self.dfs(a, s[1:], t) + self.dfs(a+s[0], s[1:], t)
        # self.ht[key] = count
        return count


"""
    2nd: recursion + memorization
    - the basic idea is to use recursion but with a hashtable to avoid redundant calculation
    - unlike the brute force approach to try all the possibilites, O(2^N), 
        here we only go forward j when s[i] == t[j] so the recursion tree is smaller

    ref:
    - https://leetcode.com/problems/distinct-subsequences/discuss/147637/DP-Recursion-%2B-Memoization

    Time    O(N^2 -> 2^N)
    Space   O(N^2)
    664 ms, faster than 5.19%
"""


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        self.ht = {}
        return self.dfs(s, t, 0, 0)

    def dfs(self, s, t, i, j):
        if j == len(t):
            return 1
        elif i == len(s):
            return 0

        key = (i, j)
        if key in self.ht:
            return self.ht[key]

        count = self.dfs(s, t, i+1, j)
        if s[i] == t[j]:
            count += self.dfs(s, t, i+1, j+1)

        self.ht[key] = count
        return count


"""
    OR
"""


class Solution:
    def numDistinct(self, S: str, T: str) -> int:
        return self.dfs(S, T, 0, 0)

    @cache
    def dfs(self, S, T, i, j):
        if j >= len(T):
            return 1
        elif i == len(S):
            return 0
        cnt = self.dfs(S, T, i+1, j)
        if S[i] == T[j]:
            cnt += self.dfs(S, T, i+1, j+1)
        return cnt


"""
    3rd: dynamic programming with an 2D array
    

      S 0123....j
    T +----------+
      |1111111111|
    0 |0         |
    1 |0         |
    2 |0         |
    . |0         |
    . |0         |
    i |0         |

              *  *
         S = [acdabefbc]
    dp[0] = [1111111111]
    dp[1] = [0111222222]

                  *  *
         S = [acdabefbc]
    dp[0] = [1111111111]
    dp[1] = [0111222222]
    dp[2] = [0000022244]

    1. first row is all one: empty target can be formed from any string
    2. first col is all zero: empty string cannot form the target
    3. when t[i] == s[j]:
        dp[i][j] = dp[i-1][j-1] <- the ways that we form target[:i-] without the the current character, i.e. string[:i])
                 + dp[i][j-1]   <- the ways that we form target[:i+1] with the current character, i.e. string[:i+1]
    4. else when t[i] != s[j]:
        dp[i][j] = dp[i][j-1]   <- the ways that we form target[:i+1] with the current character, i.e. string[:i+1]

    ref:
    - https://leetcode.com/problems/distinct-subsequences/discuss/37327/Easy-to-understand-DP-in-Java
    - https://www.youtube.com/watch?v=mPqqXh8XvWY

    Time    O(N^2)
    Space   O(N^2)
    104 ms, faster than 84.08%
"""


class Solution(object):
    def numDistinct(self, s, t):
        dp = [(len(s) + 1) * [0] for _ in range(len(t)+1)]
        for j in range(len(dp[0])):
            dp[0][j] = 1

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):

                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
                # dp[i][j] = dp[i][j-1] + (dp[i-1][j-1] if t[i-1] == s[j-1] else 0) # alternatively

        return dp[-1][-1]
