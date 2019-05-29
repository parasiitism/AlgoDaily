"""
    Give 2 numbers, implement addition without using +-*/
    - see ./idea.jpeg
    
    ref:
    - https://www.youtube.com/watch?v=qq64FrA2UXQ&t=620s
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
