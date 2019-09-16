"""
    1st: BFS
    - factorize the number by dividing it with a largest digit(from 9 to 2) iteratively
    - form the result by joining the digits together(ascending)

    Time    O(8logn)
    Space   O(logn)
    16 ms, faster than 80.85%
"""


class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a <= 1:
            return a
        arr = []
        while a > 1:
            isBroken = False
            for i in range(9, 1, -1):
                if a % i == 0:
                    arr.append(i)
                    a /= i
                    isBroken = True
                    break
            if isBroken == False:
                return 0
        arr = arr[::-1]
        res = int(''.join([str(x) for x in arr]))
        if res > 2**31-1:
            return 0
        return res
