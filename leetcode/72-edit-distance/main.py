"""
    questions to ask:
    - are the cost of add, delete, remove the same? yes
    - wil; there be empty strings? yes

    classic dynamic programming approach
    - https://www.youtube.com/watch?v=We3YDTzNXEk
    - https://www.youtube.com/watch?v=MiqoA-yF-0M
    - https://www.youtube.com/watch?v=ocZMDMZwhCY&t=9s

    Time    O(word1 * word2)
    Time    O(()word1+1) * (word2+1))
    196 ms, faster than 22.57%
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = []
        l1 = len(word1)
        l2 = len(word2)
        for i in range(l1+1):
            temp = []
            for j in range(l2+1):
                if i == 0:
                    temp.append(j)
                elif j == 0:
                    temp.append(i)
                else:
                    temp.append(0)
            dp.append(temp)

        for i in range(l1):
            for j in range(l2):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    a = dp[i][j]
                    b = dp[i][j+1]
                    c = dp[i+1][j]
                    t = min(a, b, c)
                    dp[i+1][j+1] = t+1
        return dp[-1][-1]


print(Solution().minDistance("", ""))
print(Solution().minDistance("horse", "ros"))
print(Solution().minDistance("ros", "horse"))
print(Solution().minDistance("intention", "execution"))
print(Solution().minDistance("execution", "intention"))
