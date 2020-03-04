from collections import defaultdict

"""
    1st: sort + hashtable
    1. sort the array
    2. put the indexes in a hashtable for every number
    3. for each unseen number, try to see if we can form a sequence(in length of K)

    Time    O(NlogN)
    Space   O(N)
    564 ms, faster than 21.12%
"""


class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums.sort()
        ht = defaultdict(list)
        for i in range(len(nums)):
            ht[nums[i]].append(i)
        seen = set()
        for i in range(len(nums)):
            if i in seen:
                continue
            seen.add(i)
            cur = nums[i]
            for _ in range(k-1):
                nex = cur + 1
                if nex in ht and len(ht[nex]) > 0:
                    j = ht[nex].pop(0)
                    seen.add(j)
                    cur = nex
                else:
                    return False
        return True
