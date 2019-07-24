"""
    1st approach: math

    Time    O(n)
    Space   O(n)
    784 ms, faster than 43.42%
"""


class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        hs = set()
        for x in candies:
            hs.add(x)
        return min(len(hs), len(candies)//2)


s = Solution()

a = [1, 1, 1, 1, 1, 1, 1, 1]
print(s.distributeCandies(a))

a = [1, 1, 1, 1, 1, 1, 1, 2]
print(s.distributeCandies(a))

a = [1, 1, 1, 1, 1, 1, 2, 3]
print(s.distributeCandies(a))

a = [1, 1, 1, 1, 1, 2, 3, 4]
print(s.distributeCandies(a))

a = [1, 1, 1, 1, 2, 3, 4, 5]
print(s.distributeCandies(a))

a = [1, 1, 1, 2, 3, 4, 5, 6]
print(s.distributeCandies(a))

a = [1, 1, 2, 3, 4, 5, 6, 7]
print(s.distributeCandies(a))

a = [1, 2, 3, 4, 5, 6, 7, 8]
print(s.distributeCandies(a))
