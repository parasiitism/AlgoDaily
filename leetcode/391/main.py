"""
    1st: line sweep

    Time    O(RlogR ClogC)
    Space   O(RC)
    LTE 48/40 testcases
"""
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        linesweep2D = defaultdict(Counter)
        for r1, c1, r2, c2 in rectangles:
            for i in range(r1, r2):
                linesweep2D[i][c1] += 1
                linesweep2D[i][c2] -= 1
        
        rows = sorted(linesweep2D.keys())
        prev_width = None
        prev_r = None
        for r in rows:
            
            if prev_r == None:
                prev_r = r
            elif prev_r+1 != r:
                return False
            prev_r = r

            col_idxs = sorted(linesweep2D[r].keys())
            
            pfs = 0
            back2zero = False
            for c in col_idxs:
                pfs += linesweep2D[r][c]
                if pfs == 0:
                    if back2zero:
                        return False
                    back2zero = True
                elif pfs > 1:
                    return False
            width = col_idxs[-1] - col_idxs[0]
            
            if prev_width == None:
                prev_width = width
            elif width != prev_width:
                return False
        return True

"""
    2nd: math
    - 4 corners of the combined rectangle must appear once. But corners of other rectangles must appear even number of times
    - sum of the areas must be equal to the area of the combined rectangle
"""
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corners = set()
        area_sum = 0
        for x1, y1, x2, y2 in rectangles:
            corners ^= {(x1, y1), (x1, y2), (x2, y2), (x2, y1)}
            area_sum += (x2 - x1) * (y2 - y1)        
        # check the corners
        if len(corners) != 4:
            return False
        # check area with the remaining corners
        left, bottom = 2**32, 2**32
        right, top = -(2**32), -(2**32)
        for x, y in corners:
            left = min(left, x)
            bottom = min(bottom, y)
            right = max(right, x)
            top = max(top, y)
        if (right - left) * (top - bottom) != area_sum:
            return False
        return True