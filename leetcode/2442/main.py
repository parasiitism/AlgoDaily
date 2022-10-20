"""
    hashtable + math

    Time    O(N)
    Space   O(1)
    1959 ms, faster than 20.00%
"""


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        A = nums[:]
        for x in nums:
            rev = self.rev_int(x)
            A.append(rev)
        return len(set(A))

    def rev_int(self, x):
        rev = 0
        while x > 0:
            rev = rev*10 + x % 10
            x //= 10
        return rev
