"""
    sort
    - sort the digits, split them by alternatively assign to 2 separate integers (num1, num2)
    - result = num1 + num2

    Time    O(DlogD)
    Space   O(D)
    27ms beats 100%
"""
class Solution:
    def splitNum(self, num: int) -> int:
        digits = [int(c) for c in str(num)]
        digits.sort()
        A, B = 0, 0
        for i in range(len(digits)):
            d = digits[i]
            if i % 2 == 0:
                A = 10*A + d
            else:
                B = 10*B + d
        return A + B