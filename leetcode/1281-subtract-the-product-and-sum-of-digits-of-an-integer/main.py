"""
    1st: array iteration
    Time    O(logN)
    Space   O(logN)
    20 ms, faster than 42.86%
"""
class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = []
        while n > 0:
            arr.append(n%10)
            n /= 10
        product, total = 1, 0
        for x in arr:
            product *= x
            total += x
        return product - total