"""
    base: 2 using bit op
"""


def decimal2binary(num):
    res = ''
    while num > 0:
        if num & 1 == 1:
            res = '1' + res
        else:
            res = '0' + res
        num >>= 1
    return res


print(decimal2binary(13))

"""
    base: 2 using divsion
"""


def decimal2binary(num):
    res = ''
    while num > 0:
        reminder = num % 2
        res = str(reminder) + res
        num /= 2
    return res


print(decimal2binary(13))
