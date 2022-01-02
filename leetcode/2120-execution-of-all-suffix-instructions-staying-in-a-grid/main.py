"""
    1st: graph

    Time    O(SS)
    Space   O(S) result
    1796 ms, faster than 33.33%
"""


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        res = []
        dirs = {
            'U': (-1, 0),
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1),
        }
        for i in range(len(s)):
            r, c = startPos
            steps = 0
            for j in range(i, len(s)):
                char = s[j]
                _r = r + dirs[char][0]
                _c = c + dirs[char][1]
                if _r < 0 or _r == n or _c < 0 or _c == n:
                    break
                r, c = _r, _c
                steps += 1
            res.append(steps)
        return res
