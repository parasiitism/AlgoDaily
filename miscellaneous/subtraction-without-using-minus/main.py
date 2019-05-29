"""
    Give 2 numbers, implement subtraction without using +-*/
    - a must be larger than b

    ref:
    - https://www.geeksforgeeks.org/subtract-two-numbers-without-using-arithmetic-operators/
"""


def subtract(a, b):

    # Iterate till there
    # is no carry
    while (b != 0):

        # borrow contains common
        # set bits of y and unset
        # bits of x
        borrow = (~a) & b

        # Subtraction of bits of x
        # and y where at least one
        # of the bits is not set
        a = a ^ b

        # Borrow is shifted by one
        # so that subtracting it from
        # x gives the required sum
        b = borrow << 1

    return a


print("x - y is", subtract(29, 13))
