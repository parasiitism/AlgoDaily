"""
    1st approach: brute force

    Time    O(n^2)
    Space   O(n)
    LTE
"""


class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        if S == T:
            return S
        res = S
        for i in range(len(S)):
            t = T
            for j in range(i, len(S)):
                if S[j] == t[0]:
                    t = t[1:]
                if len(t) == 0:
                    subs = S[i:j+1]
                    if len(subs) < len(res):
                        res = subs
                    break
        if res == S:
            return ""
        return res


"""
    2nd approach: dp

    Time    O(mn)
    Space   O(n)
    LTE wtf?
"""


class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        m = len(T)
        n = len(S)
        dp = []
        for i in range(m+1):
            temp = []
            for j in range(n+1):
                if i == 0:
                    temp.append(j+1)
                else:
                    temp.append(0)
            dp.append(temp)
        # print(dp)
        for i in range(1, m+1):
            for j in range(1, n+1):
                if T[i-1] == S[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        # print(dp)
        start = 0
        l = n + 1
        for j in range(1, n+1):
            if dp[m][j] != 0:
                if j - dp[m][j] + 1 < l:
                    start = dp[m][j] - 1
                    l = j - dp[m][j] + 1
        if l == n + 1:
            return ""
        return S[start: start + l]


a = "abcdebdde"
b = "bde"
print(Solution().minWindow(a, b))
