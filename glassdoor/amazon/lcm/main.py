"""
    Find the LCM between n numbers

    Questions:
    - negtive numbers?
    - zeros?
"""


class Solution(object):
    def lcm(self, nums):
        """
            a * b = lcm * gcd, we can use the gcd to find lcm using lcm = a*b/gcd
            To find the gcd, we can use Euclidian Algorithm
            100=45*2+10
            45=10*4+5
            10=5*2+0
            in the last row, the remainder is 0, therefore 5 is the common divisor

            Time    O(n)
            Space   O(1)
        """
        if len(nums) == 0:
            return 0
        res = nums[0]
        for i in range(1, len(nums)):
            res = self.findLcm(res, nums[i])
        return res

    def findLcm(self, a, b):
        if a == 0 or b == 0:
            return 0
        return a * b / self.findGcd(a, b)

    def findGcd(self, a, b):
        if a == 0 or b == 0:
            return 0
        dividend = max(a, b)
        divisor = min(a, b)
        while divisor != 0:
            remainder = dividend % divisor
            if remainder == 0:
                break
            dividend = divisor
            divisor = remainder
        return divisor


print(Solution().lcm([3, 2]))
print(Solution().lcm([0, 6]))
print(Solution().lcm([38, 85]))


# don't use GCD
# it takes a lot longer because it considers all integers
def findLCM(num1, num2):
    if num1 > num2:
        greater = num1
    else:
        greater = num2

    while True:
        if(greater % num1 == 0) and (greater % num2 == 0):
            return greater
        greater += 1


print(findLCM(54, 24))
