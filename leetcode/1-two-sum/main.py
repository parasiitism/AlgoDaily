"""
    1st approach: hashtable

    Time  O(n)
    Space O(n)
    40 ms, faster than 66.68%
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ht = {}
        for i in range(len(nums)):
            num = nums[i]
            remain = target - num
            if remain in ht:
                return [ht[remain], i]
            else:
                ht[num] = i
        return []


"""
    followup:
    - what if here might be no solution or more than one solution
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ht = {}
        res = []
        for i in range(len(nums)):
            num = nums[i]
            remain = target - num
            if remain in ht:
                res.append((ht[remain], i))
            else:
                ht[num] = i
        return res


"""
     0  1  2  3  4  5  6  7  8  9
    [5, 2, 3, 6, 7, 2, 4, 5, 8, 6]

    target = 9, pairs = (1,3), (0,2), (5, 9)
    target = 100, pairs = empty
"""
print(Solution().twoSum([5, 2, 3, 6, 7, 2, 4, 5, 8, 6], 8))

print(Solution().twoSum([5, 2, 3, 6, 7, 2, 4, 5, 8, 6], 100))
