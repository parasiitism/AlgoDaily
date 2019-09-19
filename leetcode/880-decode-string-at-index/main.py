"""
    1st: brute force

    Time    O(SK)
    Space   O(?)
    Memory Limit Exceeded
"""


class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        temp = ''
        for c in S:
            if c.isdigit():
                temp = int(c) * temp
            else:
                temp += c
            if len(temp) >= K:
                break
        return temp[K-1]


"""
    2nd: math, learned from the solution
    - when we go back, we reduce the size
        - one by one if the last character is an alphabet
        - /= if the last character is a digit
    
    case1: S = leet2code, K = 10
    - total size = 12
    - remove one by one until size = k = 10

    case2: S = leet2code, K = 2
    - total size = 12
    - remove one by one until size = 8. since the last character is a digit, we divide the size by the digit, then we get size = 4
    - when size = 4, the last character is 't', so we keep subtracting
    - subtract until size = k = 2, we done

    ref:
    - https://leetcode.com/problems/decoded-string-at-index/solution/

    Time    O(n)
    Space   O(1)
    20 ms, faster than 44.68%
"""


class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        size = 0
        for c in S:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1

        for c in reversed(S):
            K %= size
            if K == 0 and c.isalpha():
                return c
            if c.isdigit():
                size /= int(c)
            else:
                size -= 1
