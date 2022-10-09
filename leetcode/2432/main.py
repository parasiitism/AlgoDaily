"""
    math

    Time    O(N)
    Space   O(1)
    813 ms, faster than 25.00%
"""


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        cur = 0
        max_dur = 0
        res_id = -1
        for e_id, leave_t in logs:
            task_dur = leave_t - cur
            if task_dur > max_dur:
                max_dur = task_dur
                res_id = e_id
            elif task_dur == max_dur and e_id < res_id:
                res_id = e_id
            cur = leave_t
        return res_id
