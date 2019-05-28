import sys

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
    - similar to longest common subsequence
    
    e.g. S = 'abcdebdde' and T = 'bde'

    * means sys.maxsize

        _   a   b   c   d   e   b   d   d   e
    -   *   *   *   *   *   *   *   *   *   *
    b   *   *   1   2   3   4   1   2   3   3
    d   *   *   *   *   3   4   5   2   3   4
    e   *   *   *   *   *   4   5   6   7   4
                            ^               ^
    
    on 2nd row,
    - when S[i] == T[i], the first b, the min length of target subsequence = 1
    - when we have S = 'bc' and T = 'b', the min length of target subsequence = 2
    - when we have S = 'bcd' and T = 'b', the min length of target subsequence = 3
    - when we have S = 'bcde' and T = 'b', the min length of target subsequence = 4
    - when we have S = 'bcdeb' and T = 'b', the min length of target subsequence = 1 because we can just use the last 'b'

    on 3rd row,
    - when S[i] == T[i], the first d, we have S = 'bcd' and T = 'bd', 
        the m in length of target subsequence = 2 + 1 = 3 because we can use the result of S = 'bc' and T = 'b' from the previous calculation
    - same logic for the 2nd 'd', S = 'bcdebd' and T = 'bd'
    - and so on...

    so it means
    - if they match, we can use dp[i][j] = dp[i-1][j-1]+1
    - else, dp[i][j] = dp[i][j-1]+1

    We can just get the result by finding the minLength on the last row, and use slicing, S[i-minSubstringLength:i], the get the result

    Time    O(ST)
    Space   O(ST)
    2456 ms, faster than 20.68%
"""


class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        s = len(S)
        t = len(T)

        dp = []
        for _ in range(t+1):
            dp.append((s+1)*[sys.maxsize])

        for i in range(1, t+1):
            for j in range(1, s+1):
                if S[j-1] == T[i-1]:
                    if i == 1:
                        # it means this is the first character
                        dp[i][j] = 1
                    else:
                        # extend the length from previous result(which is without the current character)
                        dp[i][j] = dp[i-1][j-1]+1
                else:
                    # shortest substring if we include this character
                    dp[i][j] = dp[i][j-1]+1

        # find the min length of subsequence
        minSubstringLength = min(dp[-1])
        if minSubstringLength == sys.maxsize:
            return ''
        # get the substring by slicing
        for i in range(1, s+1):
            if dp[-1][i] == minSubstringLength:
                return S[i-minSubstringLength:i]


a = "abcdebdde"
b = "bde"
print(Solution().minWindow(a, b))
