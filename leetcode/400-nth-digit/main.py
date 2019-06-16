"""
    1st approach: math

    1 - 9       : 9 * 1
    10 - 99     : 90 * 2
    100 - 999   : 900 * 3
    1000 - 9999 : 9000 * 4
    ...

    e.g.1
    n = 1000
    1000 - (9 + 90*2) = 811
    target number = 100 + (811-1)//3 = 370
    target digit = (811-1)%3 = 0
    so the result is 3 <- (3)70

    e.g.2
    n = 3000
    3000 - (9 + 90*2 + 900*3) = 111
    target number = 1000 + (111-1)//4 = 1027.5
    target digit = (111-1)%4 = 2
    so the result is 2 <- 10(2)7

    Time    ~O(logn)
    Space   O(1)
    20 ms, faster than 66.12%
"""


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # find the range
        nine = 9
        count = 1
        start = 1
        while n > nine * count:
            n = n - nine * count
            count += 1
            nine = nine * 10
            start = start * 10
        # construct the target number
        target = start + (n-1) // count
        targetStr = str(target)
        # find out the target digit
        ith = (n-1) % count
        return int(targetStr[ith])


s = Solution()

print(s.findNthDigit(1))
print(s.findNthDigit(11))
print(s.findNthDigit(2889))
print(s.findNthDigit(3000))
print(s.findNthDigit(4000))
print(s.findNthDigit(30000))
