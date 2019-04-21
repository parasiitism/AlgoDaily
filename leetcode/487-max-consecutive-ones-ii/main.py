"""
    2nd approach: 2 pointers
    - always make sure that there is at most one 0 in the window()

    Time    O(2n)
    Space   O(1)
    344 ms, faster than 26.85%
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        left = 0
        zeroIdx = -1

        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                if zeroIdx == -1:
                    zeroIdx = i
                    if i+1 == len(nums):
                        r = i - left + 1
                        res = max(res, r)
                else:
                    r = i - left
                    res = max(res, r)
                    left = zeroIdx + 1
                    zeroIdx = i
            else:
                if i+1 == len(nums):
                    r = i - left + 1
                    res = max(res, r)
        return res


print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0]))
print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 1]))
print(Solution().findMaxConsecutiveOnes([0, 0, 1, 1, 1]))
print(Solution().findMaxConsecutiveOnes([1, 1, 1, 1, 0]))
print(Solution().findMaxConsecutiveOnes([0, 0, 1, 1, 1, 0, 0]))
print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1]))

print(Solution().findMaxConsecutiveOnes([0]))
print(Solution().findMaxConsecutiveOnes([1]))
print(Solution().findMaxConsecutiveOnes([0, 1]))
print(Solution().findMaxConsecutiveOnes([1, 0]))
print(Solution().findMaxConsecutiveOnes([1, 1, 1]))
