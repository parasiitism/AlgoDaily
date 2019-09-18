"""
    1st: simple math

    Time    O(n)
    Space   O(n)
    24 ms, faster than 63.27%
"""


class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        slots = num_people * [0]
        i = 0
        while candies > 0:
            idx = i % num_people
            if candies >= i + 1:
                slots[idx] += i+1
                candies -= i+1
            else:
                slots[idx] += candies
                candies = 0
            i += 1
        return slots
