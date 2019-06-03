"""
    1st approach: rotate every digit in each number from 1 to N

    e.g.
    699 => 966 <- it is a good number
    880 => 880 <- it is not a good number

    Time    O(nlogn) log base 10
    Space   O(logn)
    196 ms, faster than 14.69%
"""


class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        for i in range(1, N+1):
            num = self.rotate(i)
            if i != num:
                count += 1
        return count

    def rotate(self, n):
        temp = n
        arr = []
        while temp > 0:
            arr.append(temp % 10)
            temp /= 10
        arr = arr[::-1]
        m = {
            0: 0,
            1: 1,
            2: 5,
            5: 2,
            6: 9,
            8: 8,
            9: 6
        }
        res = 0
        for x in arr:
            if x not in m:
                return n
            else:
                res = res*10 + m[x]
        return res
