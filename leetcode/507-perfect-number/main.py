import math

"""
    1st approach: better brute force
    - each number is consist of root * root, 
    so the most efficient way to find out all the factors would be from 1 to root inclusively

    Time    O(n)
    Space   O(1)
    24 ms, faster than 87.03%
"""


class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False
        total = 1
        root = int(math.sqrt(num))
        for i in range(2, root+1):
            if num % i == 0:
                total += i + num//i
                if total > num:
                    return False
        return total == num


print(Solution().checkPerfectNumber(28))

"""
    2nd approach: Euclid Euler theorem

    https://en.wikipedia.org/wiki/Perfect_number

    - actually we can generate all the perfect numbers and check against the hashset

    Time    O(logn)
    Space   O(n)
    4ms beats 100%
"""


class Solution(object):
    def checkPerfectNumber(self, num):
        mersennePrimes = [2, 3, 5, 7, 13, 17]
        pNums = set()
        for p in mersennePrimes:
            temp = 2**(p-1) * (2**p-1)
            pNums.add(temp)
        print(pNums)
        if num in pNums:
            return True
        return False


print(Solution().checkPerfectNumber(28))
