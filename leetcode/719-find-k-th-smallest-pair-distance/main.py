import heapq

"""
    1st approach: brute force with heap
    - O(N^2) to get all the pairs
    - O(logN) to while we put each item into the heap

    Time    O(N^2 * log(N^2))
    LTE
"""


class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pq = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                heapq.heappush(pq, (abs(nums[i]-nums[j])))
        i = 0
        while i < k-1 and len(pq) > 1:
            heapq.heappop(pq)
            i += 1
        return heapq.heappop(pq)


s = Solution()

a = [1, 3, 1]
b = 1
print(s.smallestDistancePair(a, b))

a = [1, 3, 1]
b = 3
print(s.smallestDistancePair(a, b))

a = [1, 3, 2]
b = 3
print(s.smallestDistancePair(a, b))

a = [2, 4, 5, 8, 9]
b = 5
print(s.smallestDistancePair(a, b))

print("-----")

"""
    1st approach: binary search, learn from others
    - similar to lc378
    - the crux is we have to count the number of |nums[right] - nums[left]| less than what we guess
    - then we use binary search to find out the diff that stands at kth
    
    ref:
    - https://leetcode.com/problems/find-k-th-smallest-pair-distance/discuss/196304/Verbosely-commented-Python-Approach-3-with-example-walkthrough
    - https://leetcode.com/articles/find-k-th-smallest-pair-distance/

    Time    O(N^2 * log(N^2))
    Space   O(1)
    96 ms, faster than 90.64%
"""


class Solution(object):
    def smallestDistancePair(self, nums, k):
        # O(nlogn)
        nums.sort()
        # lower bound bsearch O(logn)
        left = 0
        right = nums[-1] - nums[0]  # the max diff we can get since its sorted
        while left < right:
            guess = (left + right) // 2
            # we do lower bsearch because we need to maintain the guess that has k number of diff
            if k <= self.numberOfDiffLessThanGuess(nums, guess):
                right = guess
            else:
                left = guess + 1
        return left

    def numberOfDiffLessThanGuess(self, nums, guess):
        # how many pairs diff, |b-a|, less than guess
        # O(2n)
        #  0, 1, 2, 3, 4 <- idx
        # [2, 4, 5, 8, 9], guess = 3
        #  ^  ^             <- count = 1-0 = 1
        #  ^     ^          <- count = 2-0 = 2
        #  ^        ^       <- 8-2 > 3, move left next
        #     ^     ^       <- 8-4 > 3, move left next
        #        ^  ^       <- count = 3-2 = 1
        #        ^    ^     <- 9-5 > 3, move left next
        #           ^ ^     <- count = 4-3 = 1
        count = left = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > guess:
                left += 1
            count += right - left
        return count


s = Solution()

a = [1, 3, 1]
b = 1
print(s.smallestDistancePair(a, b))

a = [1, 3, 1]
b = 3
print(s.smallestDistancePair(a, b))

a = [1, 3, 2]
b = 3
print(s.smallestDistancePair(a, b))

a = [2, 4, 5, 8, 9]
b = 5
print(s.smallestDistancePair(a, b))
