"""
    1st: brute force

    Time    O(N+space)
    TLE
"""


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        n = len(tasks)
        res = 0
        seen = {}
        i = 0
        while i < n:
            t_id = tasks[i]
            if t_id not in seen:
                res += 1
                seen[t_id] = res
                i += 1
            else:
                last_seen = seen[t_id]
                if res >= last_seen + space:
                    res += 1
                    seen[t_id] = res
                    i += 1
                else:
                    res += 1
        return res


"""
    2nd: hashtable
    - add the space directly

    Time    O(N)
    Space   O(N)
    955 ms, faster than 57.14% 
"""


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        res = 0
        seen = {}
        for t_id in tasks:
            if t_id not in seen:
                res += 1
                seen[t_id] = res
            else:
                last_seen = seen[t_id]
                if res >= last_seen + space:
                    res += 1
                    seen[t_id] = res
                else:
                    res = last_seen + space + 1
                    seen[t_id] = res
        return res
