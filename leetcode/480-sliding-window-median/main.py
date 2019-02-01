class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]

        1st approach
        - similar to window sum
        - but for each iteration, sort the nums
        Time    O(n*nlogn)
        Space   O(kn)
        7688ms beats 21.74%
        """
        if len(nums) == 0 or k <= 0 or k > len(nums):
            return 0
        acc = []
        res = []
        # first item
        temp = []
        for i in range(k):
            temp.append(nums[i])
        acc.append(temp)
        res.append(self.calMedian(temp))

        # 2nd item -> end
        for i in range(k, len(nums)):
            # extract the last one from acc
            # remove the first num from acc and add the current num to the acc
            # e.g. [1,2,3], 4=> 1, [2,3,4]
            clone = acc[-1][:]
            clone = clone[1:]
            clone.append(nums[i])
            # append to acc
            acc.append(clone)
            # cal median
            res.append(self.calMedian(clone))
        return res

    def calMedian(self, nums):
        sortNums = sorted(nums)
        if len(sortNums) % 2 == 0:
            half = len(sortNums)/2
            return (sortNums[half-1]+sortNums[half])/2.0
        half = len(sortNums)/2
        return float(sortNums[half])


print(Solution().medianSlidingWindow([1, 2, 3, 4, 5, 6, 7], 3))
print(Solution().medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(Solution().medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 4))
