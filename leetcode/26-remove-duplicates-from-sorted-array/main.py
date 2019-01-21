class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        1st approach:
        - just pop the duplicate items
        - return the length
        Time    O(n)
        Space   O(1)
        120ms beats 19.81%
        21jan2019
        """
        if len(nums) == 0:
            return 0
        i = 1
        cur = nums[0]
        while i < len(nums):
            if nums[i] == cur:
                nums.pop(i)  # python pop() is in-place
            else:
                cur = nums[i]
                i += 1
        return len(nums)


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
