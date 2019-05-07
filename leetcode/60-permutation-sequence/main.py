"""
    1st approach: permutation
    - actually we can get the range of permutations before we compute
    
    e.g. n=4, k=9

    permutations:
    1234
    1243
    1324
    1342
    1423
    1432
    ------ above is group 0
    2134
    2143
    2314 <- target
    2341
    2413
    2431
    ------ above is group 1
    ...

    groupIdx = (k-1)/(n-1)! = 8/3! = 1
    targetIdx = (k-1)%(n-1)! = 8%3! = 2

    Time    O((n-1)!)
    Space   O((n-1)!)
    2316 ms, faster than 8.20%
"""


class Solution(object):
    def __init__(self):
        self.result = []

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        count = 1
        for i in range(1, n):
            count *= i
        # get the group idx and result idx in the permutation group
        groupIdx = (k-1)/count
        pIdx = (k-1) % count
        # scrape out the number at groupIdx and get ready for permutation
        digits = "123456789"
        nums = digits[:n]
        head = nums[groupIdx]
        nums = nums[:groupIdx] + nums[groupIdx+1:]
        # and do permutation
        self.permute(nums, "")
        return head + self.result[pIdx]

    def permute(self, cands, chosen):
        if len(cands) == 0:
            # self.result.append(chosen)
            print(chosen)
        for i in range(len(cands)):
            can = cands[i]
            self.permute(cands[:i] + cands[i+1:], chosen + can)


print(Solution().permute("1234", ""))

print(Solution().getPermutation(3, 3))
print(Solution().getPermutation(4, 9))
print(Solution().getPermutation(9, 13596))
print(Solution().getPermutation(9, 362880))
