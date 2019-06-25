"""
    1st approach: classic bit op

    Time    O(32)
    Space   O(1)
    20 ms, faster than 95.86%
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        one = False
        while n > 0:
            if n & 1 == 1:
                if one == True:
                    return False
                one = True
            n >>= 1
        return True


"""
    2nd approach: math
    - divide by 2 until mod != 0

    Time    O(logn)
    Space   O(1) 
    20 ms, faster than 80.70% 
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n > 1:
            if n % 2 != 0:
                return False
            n //= 2
        return True


"""
    3rd approach: log

    32 = 2^5
    5 = log(32)/log(2)

    Time    O(1)
    Space   O(1)
    16 ms, faster than 92.77%
"""


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        temp = round(math.log(n, 2))
        return n == 2 ** temp
