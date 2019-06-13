"""
    1st approach: recursion

    Time    O(2^n) every number has 2 options
    Space   O(h)
    LTE
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
        return self.ifCanPartition(nums, total//2, 0)

    def ifCanPartition(self, cands, remain, curIdx):
        if remain == 0:
            return True
        if remain < 0 or len(cands) == 0 or curIdx >= len(cands):
            return False
        # choose or not choose
        return self.ifCanPartition(cands, remain - cands[curIdx], curIdx + 1)\
            or self.ifCanPartition(cands, remain, curIdx + 1)


s = Solution()

a = [1, 2, 3, 4]
print(s.canPartition(a))

a = [1, 1, 3, 4, 7]
print(s.canPartition(a))

a = [2, 3, 4, 6]
print(s.canPartition(a))

a = [1, 5, 11, 5]
print(s.canPartition(a))

a = [1, 2, 3, 5]
print(s.canPartition(a))

print("-----")

"""
    2nd approach: top-down recursion with memoization using hashtable
    - every number has 2 options
    - but we can cache the result of the combinations of remainTarget and currentIdx to avoid redundant calculation

    ref:
    - https://en.wikipedia.org/wiki/Partition_problem
    - https://www.educative.io/collection/page/5668639101419520/5633779737559040/5752754626625536

    Time    O(NS) N: number of nums, S: the total sum of all the numbers
    Space   O(h)
    32 ms, faster than 92.21%
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
        seen = {}
        return self.ifCanPartition(nums, total//2, 0, seen)

    def ifCanPartition(self, cands, remain, curIdx, seen):
        if remain == 0:
            return True
        if remain < 0 or len(cands) == 0 or curIdx >= len(cands):
            return False
        key = (remain, curIdx)

        if key in seen:
            return seen[key]

        # choose or not choose
        b = self.ifCanPartition(cands, remain - cands[curIdx], curIdx + 1, seen)\
            or self.ifCanPartition(cands, remain, curIdx + 1, seen)
        seen[key] = b
        return b


s = Solution()

a = [1, 2, 3, 4]
print(s.canPartition(a))

a = [1, 1, 3, 4, 7]
print(s.canPartition(a))

a = [2, 3, 4, 6]
print(s.canPartition(a))

a = [1, 5, 11, 5]
print(s.canPartition(a))

a = [1, 2, 3, 5]
print(s.canPartition(a))

print("-----")
