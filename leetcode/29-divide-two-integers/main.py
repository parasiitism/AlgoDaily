"""
    1st approach
	- 6 = 3*2 = 2+2+2, 7 = 3*2 = 2+2+2+1
	- be careful of the negative
	- be careful of the boundaries
	Time		O(quotient)
	Space		O(1)
	
    LTE but AC in golang?!?!
	18jun2019
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1

        if dividend < 0:
            dividend = -dividend

        if divisor < 0:
            divisor = -divisor

        cnt = 0
        while dividend >= divisor:
            dividend -= divisor
            cnt += 1

        if cnt < -(2 ^ 31):
            return -(2 ^ 31)
        elif cnt > (2 ^ 31)-1:
            return (2 ^ 31)-1

        return cnt * sign


a = -2147483648
b = -1
print(Solution().divide(a, b))
