class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        2nd approach: 2 pointers
        - slow pointer points to the right most distinct number
        - fast pointer is for iteration
        - if fast pointer meets a different value, slow pointer move forward and modify the numer as the fast pointer points to

        Time    O(n)
        Space   O(1)
        44 ms, faster than 49.13%
        18apr2019
        """
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return len(nums)
        slow = 1
        for i in range(2, len(nums)):
            num = nums[i]
            if nums[slow] == num:
                if nums[slow-1] != num:
                    slow += 1
                    nums[slow] = num
            else:
                slow += 1
                nums[slow] = num
        return slow + 1


a = [1, 1, 1, 2, 2, 3]
print(Solution().removeDuplicates(a))
print(a)

a = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(Solution().removeDuplicates(a))
print(a)
