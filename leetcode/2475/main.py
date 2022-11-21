"""
    1st: brute force

    Time    O(N^3)
    Space   O(1)
    581 ms, faster than 33.33%
"""


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    x = nums[i]
                    y = nums[j]
                    z = nums[k]
                    if x != y and y != z and x != z:
                        res += 1
        return res


"""
    2nd: hashtable + math
    - For numbers a, b and c, we can form m[a] * m[b] * m[c] unique triplets.
    e.g.
        111 222 333 444 555
      0 *** ---------------
        --- *** -----------
        ------- *** -------
        ----------- *** ---
        --------------- *** 0

    ref:
    - https://leetcode.com/problems/number-of-unequal-triplets-in-array/discuss/2831702/O(n)

    Time    O(N + UlogU) worst
    Space   O(N)
    42 ms, faster than 100.00%
"""


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        res = 0
        smaller, greater = 0, len(nums)
        ctr = Counter(nums)
        temp = sorted(ctr.items())
        for v, f in temp:
            greater -= f
            res += smaller * f * greater
            smaller += f
        return res
