"""
    1st approach: hashtable
    - count the occurence of each number

    Time    O(n)
    Space   O(n)
    48 ms, faster than 45.16%
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ht = {}
        for num in nums:
            if num not in ht:
                ht[num] = 1
            else:
                ht[num] += 1
        for key in ht:
            if ht[key] == 1:
                return key
        return -1


a = [5, 5, 5, 3]
print(Solution().singleNumber(a))

a = [2, 2, 3, 2]
print(Solution().singleNumber(a))

a = [0, 1, 0, 1, 0, 1, 99]
print(Solution().singleNumber(a))

a = [-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]
print(Solution().singleNumber(a))

print("-------------------------")

"""
    2nd approach: classic bit operation

    e.g.
        1110
        1110
        1110
    +   1001
    --------
        4331, then we mod every digit by 3, x = x%3
        1001 <- it is what we want
    
    ref:
    - http://bangbingsyb.blogspot.com/2014/11/leetcode-single-number-i-ii.html

    Time    O(32n) -> O(n)
    Space   O(1)
    116 ms, faster than 12.11%
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(31, -1, -1):
            total = 0
            mask = 1 << i
            for j in range(len(nums)):
                if nums[j] & mask > 0:
                    total += 1
            res = (res * 2) + (total % 3)
        return self.convert(res)

    def convert(self, x):
        """
            recap: how program stores negative integer?

            for int4, first digit is for polarity, other 3 are for numbers
            the funny thing is, when it becomes negative, the sequence reverses

            0111 <- 7
            0110 <- 6
            0101 <- 5
            0100 <- 4
            0011 <- 3
            0010 <- 2
            0001 <- 1
            0000 <- 0
            ---------
            1111 <- -1
            1110 <- -2
            1101 <- -3
            1100 <- -4
            1011 <- -5
            1010 <- -6
            1001 <- -7
            1000 <- -8

            in python, numbers are not stored within 2^32.

            so if, use 4 bits for simplicity, 
            we got 1101(13), we can get -3 by deducting 16, 13 - 2^4 = -3
        """
        if x >= 2**31:
            x -= 2**32
        return x


a = [5, 5, 5, 3]
print(Solution().singleNumber(a))

a = [2, 2, 3, 2]
print(Solution().singleNumber(a))

a = [0, 1, 0, 1, 0, 1, 99]
print(Solution().singleNumber(a))


a = [-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]
print(Solution().singleNumber(a))
