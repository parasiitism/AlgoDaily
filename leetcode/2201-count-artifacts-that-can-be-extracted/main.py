"""
    1st: hashtable

    Time    O(N)
    Space   O(N)
    3437 ms, faster than 41.46%
"""


class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        cells = {}

        for i in range(len(artifacts)):
            top, left, bottom, right = artifacts[i]
            for r in range(top, bottom+1):
                for c in range(left, right+1):
                    key = (r, c)
                    cells[key] = i

        for i in range(len(dig)):
            r, c = dig[i]
            key = (r, c)
            if key in cells:
                del cells[key]

        remain = set()
        for key in cells:
            val = cells[key]
            remain.add(val)

        res = set()
        for i in range(len(artifacts)):
            if i not in remain:
                res.add(i)

        return len(res)
