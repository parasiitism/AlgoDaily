"""
    Give 2 numbers, implement addition without using +-*/
"""

"""
    1st approach: XOR
    - see ./idea.jpeg
    ref:
    - https://www.youtube.com/watch?v=qq64FrA2UXQ
"""


def addTwoNumbersWithoutPlus(a, b):
    while b > 0:
        carry = a & b
        # from the right, the least significant digits would be the reult of XOR
        a = a ^ b
        # store carry in b, rmb to apply it on the next digiti so we need to left-shift
        b = carry << 1
    return a


print(addTwoNumbersWithoutPlus(4, 7))

"""
    2nd approach: hashtable + carry
"""


def addTwoNumbersWithoutPlus(a, b):
    arr = []
    carry = 0
    while a > 0 or b > 0:
        # get the least significant digit of a
        x = 0
        if a > 0:
            x = a & 1
            a >>= 1
        # get the least significant digit of b
        y = 0
        if b > 0:
            y = b & 1
            b >>= 1
        # add them by using a naive hard-coded table
        num, carry = add(x, y, carry)
        arr.append(num)
    # append the carry if it exists
    if carry > 0:
        arr.append(1)
    # binary to int
    res = 0
    for i in range(len(arr)):
        res += arr[i] * 2**i
    return res


def add(a, b, carry):
    m = {
        (0, 0, 0): (0, 0),
        (0, 1, 0): (1, 0),
        (1, 0, 0): (1, 0),
        (1, 1, 0): (0, 1),
        (0, 0, 1): (1, 0),
        (0, 1, 1): (0, 1),
        (1, 0, 1): (0, 1),
        (1, 1, 1): (1, 1),
    }
    return m[(a, b, carry)]


print(addTwoNumbersWithoutPlus(4, 7))
