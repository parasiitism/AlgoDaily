"""
    1st approach: recursion
    - similar to subset
    - but since we want subsequences, we wont sort the input array
    - to ensure each subsequnce is increasing, we check if cands[i] >= chosen[-1]
    - we use hashtable to avoid redundant result by using tuples as keys

    Time    O(n2^n) the worst case is the input array is increasing, so every number has 2 options(stay or be excluded)
    Space   O(n)
    248 ms, faster than 41.14%
"""


class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ht = {}
        self.dfs(nums, [], ht)
        res = []
        for x in ht:
            res.append(list(x))
        return res

    def dfs(self, cands, chosen, ht):
        if len(chosen) > 1:
            ht[tuple(chosen)] = chosen
        for i in range(len(cands)):
            if len(chosen) == 0 or cands[i] >= chosen[-1]:
                self.dfs(cands[i+1:], chosen + [cands[i]], ht)


s = Solution()

a = [4, 6, 7, 7]
print(s.findSubsequences(a))

a = [-2, -3, 1]
print(s.findSubsequences(a))
