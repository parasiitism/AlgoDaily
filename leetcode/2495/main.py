"""
    1st: math

    idea: the number of subarrays with even product that ends at the current index
            0  1  2  3  4  5  6
    nums = [1, 1, 2, 1, 1, 2, 1]
                +2+1
                    +3  
                       +3
                          +5+1
                             +6
    
    Time    O(N)
    Space   O(1)
"""


class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        j = -1
        for i in range(n):
            if nums[i] % 2 == 0:
                j = i
            if j != -1:
                res += j + 1
        return res


"""
    2nd: math
    - similar to 1st

            0  1  2  3  4  5  6
    nums = [1, 1, 2, 1, 1, 2, 1]
            *  *  *
                  ^  ^  ^  ^  ^

                     *  *  *
                           ^  ^
    
    Time    O(N)
    Space   O(1)
"""


class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        p = -1
        ans = 0
        n = len(nums)
        for i, num in enumerate(nums):
            if num % 2 == 0:
                ans += (i-p)*(n-i)
                p = i
        return ans
