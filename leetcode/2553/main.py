"""
    1st: int -> string

    Time    O(NC) 84ms beats 81.82%
    Space   O(NC) the result
"""


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            s = str(x)
            for c in s:
                res.append(int(c))
        return res


"""
    2nd: math

    Time    O(NC) 84ms beats 81.82%
    Space   O(NC) the result
"""


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)-1, -1, -1):
            x = nums[i]
            while x > 0:
                res.append(x % 10)
                x //= 10
        return res[::-1]
