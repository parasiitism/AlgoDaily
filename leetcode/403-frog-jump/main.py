"""
    1st approach: DFS + hashtable

    Time    O(n^2)
    Space   O(n)
    76 ms, faster than 93.81%
"""


class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        # avoid redundant calculation
        seen = set()
        # for checking
        stoneSet = set(stones)
        end = stones[-1]
        # dfs
        stack = [(0, 0)]
        while len(stack) > 0:
            loc, steps = stack.pop()
            # avoid redundant calculation
            if (loc, steps) in seen:
                continue
            seen.add((loc, steps))
            if loc == end:
                # yeah we are done
                return True
            elif loc < end:
                # 3 possible options to jump
                for i in range(steps-1, steps+2):
                    if i <= 0:
                        continue
                    if loc + i in stoneSet:
                        stack.append((loc+i, i))
        return False
