import sys
"""
    Given an array, return sum of a subarray that the absolute value of the sum is minimal

    nums = [2, -4, 6, -3, 9]

    these are some of the subarrays, (from, to):
    (0, 1), whose absolute sum = |2 + (-4)| = 2
    (0, 2), whose absolute sum = |2 + (-4) + 6| = 4
    (0, 3), whose absolute sum = |2 + (-4) + 6 + (-3)| = 1
    (1, 3), whose absolute sum = |(-4) + 6 + (-3)| = 1
    (1, 4), whose absolute sum = |(-4) + 6 + (-3) + 9| = 8
    (4, 4), whose absolute sum = |9| = 9
    Both subarrays (0, 3) and (1, 3) are min abs slices and their absolute sum equals to 1.

    note:
    - A pair of integers (P, Q), such that 0 <= P <= Q < N
"""


def f(nums):
    pfs = 0
    pfsArr = []
    for num in nums:
        pfs += num
        pfsArr.append(pfs)
    pfsArr = sorted(pfsArr)
    res = sys.maxsize
    for i in range(1, len(pfsArr)):
        temp = abs(pfsArr[i] - pfsArr[i-1])
        if temp < res:
            res = temp
        if abs(pfsArr[i]) < res:
            res = abs(pfsArr[i])
    return res


a = [2, -4, 6, -3, 9]
print(f(a))

a = [2, -4, 6, -3, 9, 0]
print(f(a))
