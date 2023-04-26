"""
    Given a list of coordinates on a cartesian plane, count the number of squares such that all 4 corners of the squares lies on the points.

    All points will have integer values, and no points will be repeated. Each point satifies -1000 <= x, y <= 1000.

    Note: the square doesn't need to be axis aligned

    e.g.
    Input: [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, 0)]

    Output: 3
    Because the 3 squares are
    [(-1,-1), (-1, 0), (0, 0), (0, -1)]
    [(-1,-0), (0, 0), (0, 1), (-1,1)]
    [(-1, 0), (0, -1), (1, 0), (0, 1)]
"""


def count_squares(points):
    point_set = set(points)
    hs = set()
    for i in range(len(points)):
        x1, y1 = points[i]
        for j in range(i + 1, len(points)):
            x2, y2 = points[j]
            dx, dy = x2 - x1, y2 - y1

            # on one side of the line
            point1 = (x1 + dy, y1 - dx)
            point2 = (x2 + dy, y2 - dx)
            if point1 in point_set and point2 in point_set:
                square = sorted([points[i], points[j], point1, point2])
                hs.add(tuple(square))

            # on the other side of the line
            point3 = (x1 - dy, y1 + dx)
            point4 = (x2 - dy, y2 + dx)
            if point3 in point_set and point4 in point_set:
                square = sorted([points[i], points[j], point3, point4])
                hs.add(tuple(square))
    # print(hs)
    return len(hs)


A = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, 0)]
print(count_squares(A))
