"""
    1st: Binary Index Tree
    - This is suboptimal because
        - I am using the full range from 1 to 10^5. i.e. if 1 <= nums[i] <= 10^9, it will get MLE
        - Also it means that if there are negative numbers, if doesn't work. i.e. if -10^9 <= nums[i] <= 10^9
    , so it leads to the 2nd approach below

    Time    O(NlogX) where X = 10^5
    Space   O(X)
    Runtime 2570ms Beats 50%
"""


class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        n = len(nums)

        forward_BIT = BinaryIndexedTree(10**5)
        forward = []
        for i in range(n):
            x = nums[i]
            forward.append(forward_BIT.getSum(x-1))
            forward_BIT.update(x, 1)

        backward_BIT = BinaryIndexedTree(10**5)
        backward = []
        for i in range(n-1, -1, -1):
            x = nums[i]
            backward.append(backward_BIT.getSum(x-1))
            backward_BIT.update(x, 1)
        backward = backward[::-1]

        res = 0
        for i in range(n):
            if forward[i] >= k and backward[i] >= k:
                res += 1
        return res


class BinaryIndexedTree(object):
    def __init__(self, n):
        self.fenwickTree = (n+1) * [0]

    def update(self, i, val):
        k = i + 1
        while k < len(self.fenwickTree):
            self.fenwickTree[k] += val
            k += k & -k

    def getSum(self, i):
        s = 0
        k = i + 1
        while k > 0:
            s += self.fenwickTree[k]
            k -= k & -k
        return s


"""
    2nd: Binary Index Tree + hashtable optimization
    - as discussed in 1st, to optimize the memory, we can create a hashtable to match a number with its sorted index, 
        so that we don't have to create 10**5 cells in the Binary Index Tree
        e.g. we transform [19,19, 7, 21] into {
            7: 1,
            19: 2,
            21: 3
        }, we just need to create BinaryIndexedTree(3) instead of BinaryIndexedTree(10^5)
    - Also, it must be faster for querying large numbers which spends log(N) time

    Time    O(NlogX) where X = the max in set(nums)
    Space   O(X)
    Runtime 2210 Beats 55.56%
"""


class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        n = len(nums)
        num2rank = {x: i+1 for i, x in enumerate(sorted(set(nums)))}

        forward_BIT = BinaryIndexedTree(len(num2rank))
        forward = []
        for i in range(n):
            x = nums[i]
            j = num2rank[x]
            forward.append(forward_BIT.getSum(j-1))
            forward_BIT.update(j, 1)

        backward_BIT = BinaryIndexedTree(len(num2rank))
        backward = []
        for i in range(n-1, -1, -1):
            x = nums[i]
            j = num2rank[x]
            backward.append(backward_BIT.getSum(j-1))
            backward_BIT.update(j, 1)
        backward = backward[::-1]

        res = 0
        for i in range(n):
            if forward[i] >= k and backward[i] >= k:
                res += 1
        return res
