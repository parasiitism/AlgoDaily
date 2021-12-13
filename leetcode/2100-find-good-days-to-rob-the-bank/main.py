"""
    1st: 2 arrays
    - forward array record a boolean at every index from security[i-k], security[i-k+1],...security[i]
    - forward array record a boolean at every index from security[i], security[i+1],...security[i+k]

    Time    O(N)
    Space   O(N)
    992 ms, faster than 12.50%
"""


class Solution:
    def goodDaysToRobBank(self, security: List[int], k: int) -> List[int]:
        n = len(security)
        if k == 0:
            return [i for i in range(n)]

        forward = n * [False]
        j = 0
        for i in range(1, n):
            if i - j == k:
                if security[i-1] >= security[i]:
                    forward[i] = True
                    j += 1
                else:
                    j = i
            else:
                if security[i-1] < security[i]:
                    j = i

        backward = n * [False]
        j = n - 1
        for i in range(n-2, -1, -1):
            if abs(i - j) == k:
                if security[i] <= security[i+1]:
                    backward[i] = True
                    j -= 1
                else:
                    j = i
            else:
                if security[i] > security[i+1]:
                    j = i

        res = []
        for i in range(n):
            if forward[i] == True and backward[i] == True:
                res.append(i)
        return res
