"""
    Iteration from the left and the right

    Time    O(N)
    Space   O(1)
"""


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        n = len(forts)
        from_left = self.count_from(forts, 0, n, 1)
        from_right = self.count_from(forts, n-1, -1, -1)
        return max(from_left, from_right)

    def count_from(self, forts, _from, _to, _dir):
        is_from_one = False
        cur = 0
        res = 0
        for i in range(_from, _to, _dir):
            x = forts[i]
            if x == 1:
                is_from_one = True
                cur = 0
            elif x == 0:
                if is_from_one == True:
                    cur += 1
            elif x == -1:
                res = max(res, cur)
                is_from_one = False
                cur = 0
        return res
