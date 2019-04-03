"""
    1st approach: brute force

    Time    O(n^2)
    Space   O(n)
    2524 ms, faster than 13.09%
"""


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        gas += gas
        cost += cost
        for i in range(n):
            acc = 0
            success = True
            for j in range(i, i+n):
                acc += gas[j] - cost[j]
                if acc < 0:
                    success = False
                    break
            if success:
                return i
        return -1


a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 1, 2]
print(Solution().canCompleteCircuit(a, b))

a = [2, 3, 4]
b = [3, 4, 3]
print(Solution().canCompleteCircuit(a, b))
