"""
    math + array

    Time    O(N)
    Space   O(1)
    135 ms, faster than 44.84%
"""


class Solution:
    def pivotInteger(self, n: int) -> int:
        total = (1+n) * n // 2
        pfs = 0
        for i in range(1, n+1):
            pfs += i
            if pfs * 2 == total + i:
                return i
            elif pfs * 2 > total + i:
                break
        return -1


"""
    math + binary search

    Time    O(logN)
    Space   O(1)
    73 ms, faster than 75.17%
"""


class Solution:
    def pivotInteger(self, n: int) -> int:
        total = (1+n)*n//2
        left, right = 1, n
        while left <= right:
            mid = (left + right)//2
            if (1+mid)*mid < total + mid:
                left = mid + 1
            elif (1+mid)*mid > total + mid:
                right = mid - 1
            else:
                return mid
        return -1
