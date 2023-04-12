"""
    Eratosthenes + binary search

    Time    O(NlogP)
    Space   O(N)
"""


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = self.gen_primes()
        prev = 0
        for i in range(len(nums)):

            # find the largest prime to subtract
            max_to_subtract = nums[i] - prev
            j = bisect_right(primes, max_to_subtract)

            # subtract the prime
            if j-1 >= 0 and primes[j-1] < max_to_subtract:
                nums[i] -= primes[j-1]
            elif j-2 >= 0 and primes[j-2] < max_to_subtract:
                nums[i] -= primes[j-2]

            # check if we meet the requiremnent
            if i > 0 and nums[i] - nums[i-1] <= 0:
                return False

            # record the current number as the previous number
            prev = nums[i]
        return True

    def gen_primes(self):
        n = 1001
        primes = n * [True]
        primes[0] = False
        primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i] == False:
                continue
            for j in range(i*i, n, i):
                primes[j] = False
        return [i for i in range(n) if primes[i]]
