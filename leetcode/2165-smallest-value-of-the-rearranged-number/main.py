"""
    1st: sort + binary search
    - 3 cases
        - 0
        - <0: reverse-sort the digits
        - >0: sort the digits, swap the first zero with the first non-zero if any

    Time    O(DlogD)
    Space   O(D)
    59 ms, faster than 33.33%
"""


class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        elif num < 0:
            s = str(-num)
            digits = [c for c in s]
            digits.sort(key=lambda x: -int(x))
            return -int(''.join(digits))
        s = str(num)
        digits = [c for c in s]
        digits.sort()
        if digits[0] != '0':
            return int(''.join(digits))
        i = self.upperBsearch(digits, 0)
        digits[0], digits[i] = digits[i], digits[0]
        return int(''.join(digits))

    def upperBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target >= int(nums[mid]):
                left = mid + 1
            else:
                right = mid
        return right
