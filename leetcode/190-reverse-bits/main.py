"""
    2nd approach:
    - create a 32bit mask
    - put the ones from the right to the correct postion(from left) in the mask
    - create the result from the mask by iterate from the right
    
	Time	O(32 + 32)
	Space	O(1)
	28 ms, faster than 22.23%
	8jun2019
"""


class Solution:
    def reverseBits(self, n):
        mask = 32 * [0]
        i = 0
        while n > 0:
            if n & 1 == 1:
                mask[i] = 1
            n >>= 1
            i += 1
        res = 0
        for i in range(31, -1, -1):
            res += mask[i] * 2**(31-i)
            i += 1
        return res
