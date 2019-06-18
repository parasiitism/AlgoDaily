"""
    1st approach: hashtable

    Time    O(n) n might be 2^31-1 at most
    Space   O(n)
    LTE
"""


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if lower > upper:
            return []
        start = None
        end = None
        hs = set(nums)
        res = []
        for i in range(lower, upper+1):
            if i not in hs:
                if start == None:
                    start = i
                    end = i
                else:
                    end = i
            else:
                if start != None:
                    if start < end:
                        res.append(str(start)+"->"+str(end))
                    else:
                        res.append(str(start))
                    start = None
                    end = None
        if start != None:
            if start < end:
                res.append(str(start)+"->"+str(end))
            else:
                res.append(str(start))
        return res


"""
    2nd approach: array

    Time    O(n) number of nums
    Space   O(1)
    16 ms, faster than 86.02%
"""


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if lower > upper:
            return []
        nums = [lower-1] + nums + [upper+1]
        res = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 2:
                res.append(str(nums[i-1]+1))
            elif nums[i] - nums[i-1] > 2:
                res.append(str(nums[i-1]+1) + '->' + str(nums[i]-1))
        return res
