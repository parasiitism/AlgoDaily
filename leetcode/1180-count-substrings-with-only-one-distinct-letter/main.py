"""
    1st: brute force

    Time    O(N^2)
    Space   O(1)
    304 ms, faster than 11.52%
"""


class Solution(object):
    def countLetters(self, S):
        """
        :type S: str
        :rtype: int
        """
        count = 0
        for i in range(len(S)):
            for j in range(i, len(S)):
                if S[i] == S[j]:
                    count += 1
                else:
                    break
        return count


"""
    2nd: math

    Time    O(N)
    Space   O(1)
    20 ms, faster than 52.73%
"""


class Solution(object):
    def countLetters(self, S):
        """
        :type S: str
        :rtype: int
        """
        res = 0
        cur, count = S[0], 1
        for i in range(1, len(S)):
            if S[i] != cur:
                res += count * (count + 1) / 2
                cur, count = S[i], 1
            else:
                count += 1
        return res + count * (count + 1) / 2
