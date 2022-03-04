from collections import Counter
from math import ceil


def f():
    _ = input()
    nums = [int(s) for s in input().split(" ")]
    cntr = Counter(nums)
    res = 0

    # all 4s
    res += cntr[4]

    # 3 + 1
    max3n1 = min(cntr[3], cntr[1])
    res += max3n1
    cntr[1] -= max3n1
    cntr[3] -= max3n1
    if cntr[3] > 0:
        res += cntr[3]
        cntr[3] = 0

    # 2 + 2
    max2n2 = cntr[2] // 2
    res += max2n2
    cntr[2] %= 2

    # 2 + 1
    if cntr[2] > 0:  # there will be at most 1
        if cntr[1] > 0:
            res += 1
            cntr[2] -= 1
            cntr[1] -= min(cntr[1], 2)
        else:
            res += 1
            cntr[2] -= 1

    # all 1s
    res += ceil(cntr[1] / 4)

    return res


print(f())
