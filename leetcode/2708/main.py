"""
    1st: recursion
    
    Time    O(2^N)
    Space   O(2^N) the tree
"""


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        res = -2**32

        def dfs(n, remain):
            nonlocal res
            res = max(res, n)
            for i in range(len(remain)):
                used = n * remain[i]
                dfs(used, remain[i+1:])

        for i in range(len(nums)):
            dfs(nums[i], nums[i+1:])

        return res


"""
    2nd: greedy
    - the idea is product all the non-zero numbers, and if the product is negative then return product / least negative
    - the corner case is the presence zeros

    learned from
    https://leetcode.com/problems/maximum-strength-of-a-group/solutions/3568549/explained-product-of-all-non-zero-o-n-very-simple-easy-to-understand-solution/

    Time    O(N)
    Space   O(1)
"""


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        product = 1
        leastNegative = -2**32
        largest = -2**32
        neg_cnt = 0
        for x in nums:
            if x != 0:
                product *= x
            if x < 0:
                leastNegative = max(leastNegative, x)
                neg_cnt += 1
            largest = max(largest, x)
        if largest == 0 and neg_cnt < 2:
            return 0
        if product > 0:
            return product
        return product // leastNegative
