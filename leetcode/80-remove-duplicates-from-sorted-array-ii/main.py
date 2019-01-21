class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        1st approach:
        - use a hashtable
        - just pop the duplicate items which occurence > 2
        - return the length
        Time    O(n)
        Space   O(n)
        120ms beats 9.74%
        21jan2019
        """
        if len(nums) == 0:
            return 0
        ht = {nums[0]: 1}
        i = 1
        while i < len(nums):
            num = nums[i]
            if num in ht:
                if ht[num] < 2:
                    ht[num] += 1
                    i += 1
                else:
                    nums.pop(i)
            else:
                ht[num] = 1
                i += 1
        return len(nums)


a = [1, 1, 1, 2, 2, 3]
print(Solution().removeDuplicates(a))
print(a)

a = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(Solution().removeDuplicates(a))
print(a)
