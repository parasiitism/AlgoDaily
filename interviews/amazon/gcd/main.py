"""
    Found the greatest common divisor between 2 numbers

    Questions:
    - negtive numbers?
    - zeros?
"""


def findGCD(num1, num2):
    """
        Euclidian Algorithm
        - be careful of the corner cases
    """
    if num1 == num2:
        return num1
    if num1 == 0 or num2 == 0:
        return 0

    dividend = 0
    divisor = 0
    if num1 < num2:
        dividend = num2
        divisor = num1
    else:
        dividend = num1
        divisor = num2

    while True:
        mode = dividend % divisor
        if mode == 0:
            break
        else:
            dividend = divisor
            divisor = mode

    return divisor


print(findGCD(34, 306))
print(findGCD(1701, 3768))
print(findGCD(-1701, 3768))  # ?
print(findGCD(1701, -3768))  # ?
print(findGCD(-1701, -3768))  # ?
print(findGCD(1, 2))
print(findGCD(34, 34))
print(findGCD(0, 306))
print(findGCD(34, 0))
