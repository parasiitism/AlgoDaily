"""
    1st: sort + math

    1) get the sum of top k largest numbers res. If result is even, just return it
    2) Otherwise, ressult is odd and we just need to change one number
        - replace the smallest even number from res by the largest odd number from the rest of the array, or
        - replace the smallest odd number from res by the largest even number from the rest of the array
    
    Time    O(NlogN)
    Space   O(N)
    664 ms, faster than 100.00%
"""


class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        A = sorted(nums, key=lambda x: -x)
        res = sum(A[:k])
        if res % 2 == 0:
            return res

        smallest_odd = 2**32
        smallest_even = 2**32
        for i in range(k):
            if A[i] % 2 == 1:
                smallest_odd = min(smallest_odd, A[i])
            else:
                smallest_even = min(smallest_even, A[i])
        ans = -1
        for i in range(k, n):
            if A[i] % 2 == 1 and smallest_even != 2**32:
                ans = max(ans, res - smallest_even + A[i])
            if A[i] % 2 == 0 and smallest_odd != 2**32:
                ans = max(ans, res - smallest_odd + A[i])
        return ans
