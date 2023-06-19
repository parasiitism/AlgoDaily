"""
    array simulation

    Time    O(~N^2)
    Space   O(N)
"""


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        received = n * [False]
        cur = 1
        i = 1
        while received[cur-1] == False:
            received[cur-1] = True
            cur = (cur + i*k) % n
            i += 1
        res = []
        for i in range(n):
            if received[i] == False:
                res.append(i+1)
        return res
