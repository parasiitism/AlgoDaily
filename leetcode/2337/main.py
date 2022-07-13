"""
    greedy
    - compare the indices for each of the L or R

    5050 ms, faster than 14.29% 
"""


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        processed = []
        for i in range(n):
            x = target[i]
            if x in 'LR':
                processed.append((x, i))
        processed_cnt = len(processed)
        cnt = 0
        for i in range(n):
            x = start[i]

            if x in 'LR' and len(processed) == 0:
                return False

            if x == 'L':
                y, j = processed.pop(0)
                cnt += 1
                if y != 'L' or i < j:
                    return False
            if x == 'R':
                y, j = processed.pop(0)
                cnt += 1
                if y != 'R' or i > j:
                    return False
        return processed_cnt == cnt
