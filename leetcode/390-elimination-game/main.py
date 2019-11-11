"""
    1st: brute force
    Time    O(n^2)
    Space   O(n)
    LTE
"""
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = []
        for i in range(n):
            nums.append(i+1)
        while len(nums) > 1:
            arr = []
            for i in range(len(nums)):
                if i%2 == 0:
                    arr.append(nums[i])
            print(arr)
            nums = arr[::-1]
        return nums[0]


s = Solution()
print(s.lastRemaining(10))
print(s.lastRemaining(11))

"""
    2nd: recursion + math

    Time    O(logN)
    Space   O(logN)
    36 ms, faster than 33.63%
"""
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.leftToRight(n)

    def leftToRight(self, n):
        if n <= 2:
            return n
        return 2 * self.rightToLeft(n / 2)

    def rightToLeft(self, n):
        if n <= 2:
            return 1
        if n % 2 == 1:
            return 2 * self.leftToRight(n / 2)
        return 2 * self.leftToRight(n / 2) - 1

s = Solution()
print(s.lastRemaining(10))
print(s.lastRemaining(11))

"""
    3rd: recursion + math
    - advanced form of the 2nd approach

    Time    O(logN)
    Space   O(logN)
    32 ms, faster than 49.78%
"""
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 1 if n == 1 else 2*(n/2 + 1 - self.lastRemaining(n/2))

s = Solution()
print(s.lastRemaining(10))
print(s.lastRemaining(11))