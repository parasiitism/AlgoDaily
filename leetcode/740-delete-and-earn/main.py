from collections import defaultdict

"""
    1st: dynamic programming
    1. for each distinct number, accumulate the sum
        e.g. [2, 2, 3, 3, 3, 5, 7, 8, 8]
        -> [ (2, 4), (3,9), (5, 5), (7, 7), (8, 16)] <- (distinct number, sum)
    2. sort them
    3. do lc198: house robber

    Time    O(NlogN)
    Space   O(N)
    56 ms, faster than 67.73%
"""


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # calculate the total for each distinct number, and sort them
        if len(nums) == 0:
            return 0
        ht = defaultdict(int)
        for num in nums:
            ht[num] += num
        arr = []
        for key in ht:
            arr.append((key, ht[key]))
        arr = sorted(arr)

        # house robber
        included = arr[0][1]
        excluded = 0
        for i in range(1, len(arr)):
            temp = included
            if arr[i][0] > arr[i-1][0] + 1:
                included += arr[i][1]
            else:
                included = max(excluded + arr[i][1], included)
            excluded = temp
        return included
