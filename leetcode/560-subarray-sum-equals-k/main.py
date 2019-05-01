"""
    1st approach: zero sum subarray
    - this question is fucking similar to leetcode 325, 525
    - the basic idea is to store the previous sum in a hashtable
        e.g. key: previous sum, value: number of occurence of a previous sum
    - if currentSum - target in the hastable, the result += occurence

    e.g. [1, -1, 5, -2, 1, 2], 3
    when it comes to 2, remain = 6 - 3 = 3 and 3 is in the hashtable what does it mean?

    consider that a = [1,-1,5,-2] = 3,  b = [1, -1, 5, -2, 1, 2] = 6, 
    6-3 means the remain from a - b, which is [1,2], is = target k
    
    ref:
    - https://www.youtube.com/watch?v=hLcYp67wCcM

    Time	O(n)
    Space O(n)
    36ms beats 96.05%
    28jan2019
"""


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        acc = 0
        # key: previous sum, value: number of occurence of a previous sum
        ht = {}
        for i in range(len(nums)):
            acc += nums[i]
            # if acc == k, it is one of the target subarray
            if acc == k:
                res += 1
            # if acc-k in hashtable, it is one of the target subarray
            remain = acc-k
            if remain in ht:
                res += ht[remain]
            # put the acc into the hashtable
            if acc not in ht:
                ht[acc] = 1
            else:
                ht[acc] += 1
        return res


print(Solution().subarraySum([1, 1, 1], 1))  # 3
print(Solution().subarraySum([1, 1, 1], 2))  # 3
print(Solution().subarraySum([1, 1, 1], 3))  # 1
print(Solution().subarraySum([1, 1, 1, 1], 3))  # 2
print(Solution().subarraySum([1, -1, 5, -2, 3], 3))  # 3
print(Solution().subarraySum([1, -1, 5, -2, 1, 2], 3))  # 3
print(Solution().subarraySum([-2, -1, 2, 1], 1))  # 2
print(Solution().subarraySum([-2, -1, 2, 1, 100], 100))  # 2
print(Solution().subarraySum([-2, -1, 2, 100, 1], 100))  # 2
print(Solution().subarraySum([-2, -1, 2, 1000], 99))  # 0

print("-----")

"""
    2nd approach
    - this question is fucking similar to leetcode 325
    - the basic idea is to store the previous sum in a hashtable
        e.g. key: previous sum, value: number of occurence of a previous sum
    - if currentSum - target in the hastable, the result+1
    
    Time	O(n)
    Space O(n)
    36ms beats 96.05%
    28jan2019
"""


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        acc = 0
        # key: previous sum, value: number of occurence of a previous sum
        ht = {}
        ht[0] = 1  # if acc == k remain = 0, it is one of the target subarray
        for i in range(len(nums)):
            acc += nums[i]
            # if acc-k in hashtable, it is one of the target subarray
            if acc-k in ht:
                res += ht[acc-k]
            # put the acc into the hashtable
            if acc not in ht:
                ht[acc] = 1
            else:
                ht[acc] += 1
        return res


print(Solution().subarraySum([1, 1, 1], 1))  # 3
print(Solution().subarraySum([1, 1, 1], 2))  # 3
print(Solution().subarraySum([1, 1, 1], 3))  # 1
print(Solution().subarraySum([1, 1, 1, 1], 3))  # 2
print(Solution().subarraySum([1, -1, 5, -2, 3], 3))  # 3
print(Solution().subarraySum([-2, -1, 2, 1], 1))  # 2
print(Solution().subarraySum([-2, -1, 2, 1, 100], 100))  # 2
print(Solution().subarraySum([-2, -1, 2, 100, 1], 100))  # 2
print(Solution().subarraySum([-2, -1, 2, 1000], 99))  # 0
