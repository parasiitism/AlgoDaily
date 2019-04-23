import random

"""
    1st approach: use random.shuffle LOL

    Time    O(n)
    Space   O(n)
    244 ms, faster than 99.22%
"""


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        items = self.nums[:]
        random.shuffle(items)
        return items


items = [1, 2, 3]
i = random.randint(0, len(items)-1)
print(i)

"""
    2nd approach: Fisher-Yates Algorithm
    - python builtin random.shuffle() actaully does Fisher-Yates Algorithm
    - what it does is
    1. in each iteration, randomly generate an index, j,from i to len(nums)-1
    2. swap the items at i and j

    ref:
    - https://leetcode.com/articles/shuffle-an-array/

    Time    O(n)
    Space   O(n)
    324 ms, faster than 87.02%
"""


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        items = self.nums[:]
        for i in range(len(items)):
            j = random.randint(i, len(items)-1)
            items[i], items[j] = items[j], items[i]

        return items
