"""
    2nd approach
	- for earch item in the array, cache the sum from start

	Time of Constructor O(n)
	Space of Constructor O(n)
	Time of SumRange O(1)
	Space of SumRange O(1)
	68 ms, faster than 67.78%
"""


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        prefixSums = []
        prefixSum = 0
        for num in nums:
            prefixSum += num
            prefixSums.append(prefixSum)
        self.prefixSums = prefixSums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i < 0 or i+1 > len(self.prefixSums) or j < 0 or j+1 > len(self.prefixSums):
            return
        if i == 0:
            return self.prefixSums[j]
        else:
            return self.prefixSums[j] - self.prefixSums[i-1]
