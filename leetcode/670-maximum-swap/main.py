"""
    1st approach: brute-force
    - try all the pairs to swap
    - find the max number
    - since the input is at most 1x10^8, there are at most 8*7 trials

    Time    O(logn x logn x logn)
    Space   O(logn) save the digit
    20 ms, faster than 49.64%
"""


class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        arr = []
        s = str(num)
        digits = [x for x in s]
        res = num
        for i in range(len(digits)):
            for j in range(i, len(digits)):
                clone = digits[:]
                clone[i], clone[j] = clone[j], clone[i]
                temp = int(''.join(clone))
                if temp > res:
                    res = temp
        return res
