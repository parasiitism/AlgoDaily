from typing import List

"""
    1st: recursion
    - use subset

    Time    O(2^N)
    Space   O(2^N)
    TLE
"""


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        self.res = 0
        self.dfs(nums, 0)
        return self.res

    def dfs(self, nums: List[int], chosenSum: int):
        if chosenSum % 3 == 0:
            self.res = max(self.res, chosenSum)
        for i in range(len(nums)):
            # split the numbers
            # e.g. 1234 -> 1 234
            # process 234 in the further recursion
            # add 1 to the path
            self.dfs(nums[i+1:], chosenSum + nums[i])


"""
    2nd: dynamic programming

    1.The last maximum possible sum that it is divisible by 3 depends on 3 subproblems:
        1. previous maximum sum that it is divisible by 3
            preSum % 3 == 0      (example: preSum=12 if lastNum=3)
        2. preSum % 3 == 1       (example: preSum=13 if lastNum=2)
        3. preSum % 3 == 2       (example: preSum=14 if lastNum=1)
    2. This "subproblems" pattern hints Dynamic Programming

    f[i] is the biggest value can possibly have after ith iteration, with remainder 0,1,2.

    For example, the input is 3,6,5,1,8. The initial f would be
    [[3,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0]]

    After the first iteration, which the ith value is 6. The f would become
    [[3,0,0],
    [9,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0]]

    After 2nd iteration, when ith value is 5, f becomes
    [[3,0,0],
    [9,0,0],
    [9,0,14], (14 is from 9 + 5)
    [0,0,0],
    [0,0,0]]

    Then, ith value is 1
    [[3,0,0],
    [9,0,0],
    [9,0,14],
    [15,10,14], (15 is from 14 + 1, 10 is from 9 + 1)
    [0,0,0]]

    And finally, ith value is 8
    [[3,0,0],
    [9,0,0],
    [9,0,14],
    [15,10,14],
    [18,22,23]] (18 is from 10 + 8, 22 is from 14 + 8, 23 is from 15 + 8)

    ref:
    - https://leetcode.com/problems/greatest-sum-divisible-by-three/discuss/431077/JavaC%2B%2BPython-One-Pass-O(1)-space

    Time    O(3N)
    Space   O(3)
    396 ms, faster than 55.73%
"""


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        seen = [0, 0, 0]
        for a in nums:
            for x in seen[:]:
                cur = x + a
                mod = cur % 3
                seen[mod] = max(seen[mod], cur)
        return seen[0]
