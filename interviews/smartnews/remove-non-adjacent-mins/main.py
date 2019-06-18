import sys

"""
    https://www.1point3acres.com/bbs/interview/machine-learning-485949.html

    a = [3, 2, 1, 4, 3 ,5, -2, -1, 10, 9]
               ^            ^
"""


def f(nums):
    """
        1st approach: sort + compare
        - sort
        - compare, the result must be from the 3 smallest items

        e.g. [....-3,-4,-3,.....]

        -3-4 = -7 but they are adajent
        -4-3 = -7 but they are adajent
        -3-3 = -6 they are non-adajent finally

        Time    O(nlogn)
    """
    arr = []
    for i in range(1, len(nums)-1):
        arr.append([nums[i], i])
    arr = sorted(arr, key=lambda x: x[0])
    a = arr[0]
    b = arr[1]
    c = arr[2]
    if abs(a[1] - b[1]) > 1:
        return a[0] + b[0], a[1], b[1]
    elif abs(a[1] - c[1]) > 1:
        return a[0] + c[0], a[1], c[1]
    elif abs(b[1] - c[1]) > 1:
        return b[0] + c[0], b[1], c[1]


a = [3, 2, 1, 4, 3, 5, -2, -1, 10, 9]
print(f(a))

a = [3, 2, -2, -4, -3, 5, -2, -1, 10, 9]
print(f(a))

a = [3, 2, -3, -4, -3, -2, -1, 0, 10, 9]
print(f(a))

a = [3, 2, -3, -3, -3, -3, -1, 0, 10, 9]
print(f(a))

print("-----")


def f(nums):
    """
        1st approach: get the 3 min values + compare
        - get the 3 min values in a loop
        - compare, the result must be from the 3 smallest items

        e.g. [....-3,-4,-3,.....]

        -3-4 = -7 but they are adajent
        -4-3 = -7 but they are adajent
        -3-3 = -6 they are non-adajent finally

        Time    O(n)
    """
    a = (sys.maxsize, -1)
    b = (sys.maxsize, -1)
    c = (sys.maxsize, -1)
    for i in range(1, len(nums)-1):
        num = nums[i]
        if num < a[0]:
            c = b
            b = a
            a = (num, i)
        elif num < b[0]:
            c = b
            b = (num, i)
        elif num < c[0]:
            c = (num, i)

    if abs(a[1] - b[1]) > 1:
        return a[0] + b[0], a[1], b[1]
    elif abs(a[1] - c[1]) > 1:
        return a[0] + c[0], a[1], c[1]
    elif abs(b[1] - c[1]) > 1:
        return b[0] + c[0], b[1], c[1]


a = [3, 2, 1, 4, 3, 5, -2, -1, 10, 9]
print(f(a))

a = [3, 2, -2, -4, -3, 5, -2, -1, 10, 9]
print(f(a))

a = [3, 2, -3, -4, -3, -2, -1, 0, 10, 9]
print(f(a))

a = [3, 2, -3, -3, -3, -3, -1, 0, 10, 9]
print(f(a))

print("-----")
