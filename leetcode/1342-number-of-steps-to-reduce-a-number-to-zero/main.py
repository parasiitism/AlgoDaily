"""
    1st: iteration
    - as straight forward as the title

    Time    O(logN)
    Space   O(1)
    24 ms beats 87.42%
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            count += 1
        return count


"""
    2nd: recursion
    - as straight forward as the title but in recursive manner

    Time    O(logN)
    Space   O(1)
    28 ms beats 64.85%
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 2 == 0:
            return self.numberOfSteps(num//2) + 1
        return self.numberOfSteps(num-1) + 1


"""
    3rd: bit operation
    
    e.g. 43

    1   0   1   0   1   1   <- binary prepresentation of 43
    -1  /2  -1  /2  -1  -1  <- first step
    /2      /2      /2  /2  <- second steps

    so the 43 takes 10 - 1 = 9 to 0

    Time    O(logN)
    Space   O(1)
    28 ms beats 64.85%
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        count = 0
        while num > 0:
            if num & 1 == 1:
                count += 2
            else:
                count += 1
            num >>= 1
        return count - 1
