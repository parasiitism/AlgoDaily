"""
    Given a circle with x, y, r indicating the coordinate of the center (x, y) and the radius (r),
    find the number of coordinates with non-negative integer coordinates in the circle

    LTE
"""


def f(x, y, r):
    left = max(x-r, 0)
    right = max(x+r+1, 0)
    bottom = max(y-r, 0)
    up = max(y+r+1, 0)

    res = 0
    for i in range(left, right):
        for j in range(bottom, up):
            dd = (i - x)**2 + (j - y)**2
            if dd <= r*r:
                res += 1
    return res


print(f(2, 3, 1))

"""
    TODO: binary search
"""
