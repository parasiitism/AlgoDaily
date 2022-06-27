from itertools import count

"""
    2 pointers
    
    Time    O(N)
    Space   O(N)
"""


def f():
    _, t = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    res = 0
    cur = 0
    j = 0
    for i in range(len(nums)):
        cur += nums[i]
        while cur > t:
            cur -= nums[j]
            j += 1
        res = max(res, i - j + 1)
    return res


print(f())
