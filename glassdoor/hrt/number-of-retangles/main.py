from collections import *

"""
    Given a list of coordinates on a cartesian plane, count the number of squares such that all 4 corners of the rectangles lies on the points.

    All points will have integer values, and no points will be repeated. Each point satifies -1000 <= x, y <= 1000.

    Note: the rectangle doesn't need to be axis aligned

    e.g.
    Input: [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, 0)]

    Output: 4
    Because the 3 rectangles are
    [(-1,-1), (-1, 0), (0, 0), (0, -1)]
    [(-1,-0), (0, 0), (0, 1), (-1,1)]
    [(-1, 0), (0, -1), (1, 0), (0, 1)]
    [(-1, 0), (0, -1), (0, 1), (-1, 1)]
"""


def get_dist_and_center(x1, x2, y1, y2):
    dist2 = (x1 - x2)**2 + (y1 - y2)**2
    center = ((x1 + x2)/2.0, (y1 + y2)/2.0)
    return (dist2, center)


def count_rectangles(points):
    n = len(points)
    ctr = Counter()
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i+1, n):
            x2, y2 = points[j]
            # For a rectange(including square), the center and 2 diagonal lines must be the same
            dist2, center = get_dist_and_center(x1, x2, y1, y2)
            key = (dist2, center)
            ctr[key] += 1
    res = 0
    for key in ctr:
        no_of_lines = ctr[key]
        res += no_of_lines * (no_of_lines - 1) // 2
    return res


A = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, 0)]
print(count_rectangles(A))
