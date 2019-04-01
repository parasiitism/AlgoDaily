import bisect


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]

        1st approach
        - similar to window sum
        - but for each iteration, sort the nums
        Time    O(n*klogk)
        Space   O(k)
        TLE
        """
        if len(nums) == 0 or k <= 0 or k > len(nums):
            return 0
        res = []
        # first result(first k items' median)
        window = []
        for i in range(k):
            window.append(nums[i])
        res.append(self.calMedian(window[:]))

        # 2nd item -> end
        for i in range(k, len(nums)):
            # remove the first num from window and add the current num to the window
            # e.g. [1,2,3], 4=> 1, [2,3,4]
            window.pop(0)
            window.append(nums[i])
            # copy window and cal median of the copy
            res.append(self.calMedian(window[:]))
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

print("----------------------------------------")


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]

        2nd approach
        - similar to 1st approach but use binary search to 
            - pop the left most item
            - push the right most item to the window
        - therefore to optimize the window sliding

        Time    O(n*2logk)
        Space   O(k)

        200 ms, faster than 57.24%
        """
        if len(nums) == 0 or k <= 0 or k > len(nums):
            return 0
        medians, window = [], []

        for i in range(len(nums)):

            # find position where outgoing element should be removed from
            if i >= k:
                # O(k) remove
                # window.remove(nums[i-k])

                # O(logk) remove with binary search
                idx = bisect.bisect_left(window, nums[i - k])
                window.pop(idx)

            # maintain the sorted invariant while inserting incoming element with binary search
            # O(logk)
            # or x = bisect.bisect_right(window, nums[i]) and window.insert(x, nums[i])
            bisect.insort(window, nums[i])

            # find the medians
            if i >= k - 1:
                half = k/2
                temp = 0.0
                if k % 2 == 0:
                    temp = (window[half-1] + window[half]) / 2.0
                else:
                    temp = float(window[half])
                medians.append(temp)

        return medians


print(Solution().medianSlidingWindow([1, 2, 3, 4, 5, 6, 7], 3))
print(Solution().medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(Solution().medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 4))
