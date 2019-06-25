"""
    1st approach: math
	- we rephrase it as it asks how many 2*5=10s are within N
	- since 2 are everywhere, it actually asks how many 5s are with N
	e.g. N = 30
	1,2,3,4,5,6,7,8,9,10
	11,12,13,14,15,16,17,18,19,20
	21,22,23,24,25,26,27,28,29,30

	5,10,15,20,25,30 there are 6 fives(25 has 2 fives)

	Time	O(logn/log5) <- log base 5
	Space	O(1)
	0 ms, faster than 100.00%
"""


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count
