"""
    Time    O(2R * sqrt(X))
    - just traverse the diagonal axis
    - primality test: https://en.wikipedia.org/wiki/Primality_test
"""


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        R, C = len(nums), len(nums[0])
        res = 0
        for i in range(R):
            left2right = nums[i][i]
            if self.is_prime(left2right):
                res = max(res, left2right)
            right2left = nums[i][C-i-1]
            if self.is_prime(right2left):
                res = max(res, right2left)
        return res

    def is_prime(self, n: int) -> bool:
        if n <= 3:
            return n > 1
        if n % 2 == 0 or n % 3 == 0:
            return False
        limit = int(n**0.5)
        for i in range(5, limit+1, 6):
            if n % i == 0 or n % (i+2) == 0:
                return False
        return True
