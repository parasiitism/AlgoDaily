"""
    math
    - try all numbers starting from x >= half

    Time    O(N/2)
    Space   O(1)
    7165 ms, faster than 100.00%
"""


class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        x = num // 2
        while x <= num:
            rev = 0
            temp = x
            while temp > 0:
                rev = rev*10 + temp % 10
                temp //= 10

            if x + rev == num:
                return True
            x += 1
        return False
