"""
    2nd approach: 2 pointers
    - slow pointer points to the right most distinct number
    - fast pointer is for iteration
    - if fast pointer meets a different value, slow pointer move forward and modify the numer as the fast pointer points to

    Time    O(n)
    Space   O(1)
    84 ms, faster than 33.44%
    18apr2019
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        slow = 0
        for i in range(1, len(nums)):
            num = nums[i]
            if nums[slow] != num:
                slow += 1
                nums[slow] = num
        return slow + 1


a = []
s = Solution().removeDuplicates(a)
print(a)

a = [1]
s = Solution().removeDuplicates(a)
print(a)

a = [1, 1]
s = Solution().removeDuplicates(a)
print(a)

a = [1, 2]
s = Solution().removeDuplicates(a)
print(a)

a = [1, 1, 2]
s = Solution().removeDuplicates(a)
print(a)

a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
s = Solution().removeDuplicates(a)
print(a)

a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4]
s = Solution().removeDuplicates(a)
print(a)
