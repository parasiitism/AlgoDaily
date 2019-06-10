"""
    1st approach: greedy
    
    e.g.1
    num = 14267
           ^
    the arrow points to the digit that its the last modified digit (from the right)
    , so we -1 on that digit, 13267, and set the all digits on its right to 9 => 13999

    e.g.2
    num = 1444267
           ^
    the arrow points to the digit that its the last modified digit (from the right)
    , 1333267, we set all the digits on its right to 9, => 13999

    e.g.3
    num = 120
           ^
    the arrow points to the digit that its the last modified digit (from the right)
    , 110, we set all the digits on its right to 9, => 119

    ref:
    - https://blog.csdn.net/fuxuemingzhu/article/details/82721627

    Time    O(logn) base10, the number of digits of a decimal number
    Space   O(logn) base10, the number of digits of a decimal number
    16 ms, faster than 94.31% 
"""


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

        # get the digits(in reversed order)
        nums = []
        while N > 0:
            nums.append(N % 10)
            N /= 10
        # modifty the digits and get the position of the last modified digit
        digits = []
        lastDigit = 9
        j = 0
        for i in range(len(nums)):
            digit = nums[i]
            if digit <= lastDigit:
                digits.append(digit)
                lastDigit = digit
            else:
                digits.append(digit-1)
                lastDigit = digit-1
                j = i
        # set all the digits to 9 on the right of the last modified digit
        for i in range(j):
            digits[i] = 9
        # constrcut the number
        digits = digits[::-1]
        res = 0
        for d in digits:
            res = res*10 + d
        return res


s = Solution()

print(s.monotoneIncreasingDigits(9))
print(s.monotoneIncreasingDigits(10))
print(s.monotoneIncreasingDigits(120))
print(s.monotoneIncreasingDigits(1234))
print(s.monotoneIncreasingDigits(332))
print(s.monotoneIncreasingDigits(10000))
print(s.monotoneIncreasingDigits(14267))
print(s.monotoneIncreasingDigits(1444267))
