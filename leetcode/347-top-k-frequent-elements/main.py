import heapq
import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        1st approach
        - count num: freq into a hashtable
        - put the hashtable key&value into a priority queue
        - the first k elements are the top k elements in the priority queue

        36ms beats 82.56%
        1feb2019
        """
        if k > len(nums):
            return []
        maxOccur = 0
        ht = {}
        pq = []
        # count the freq for each num
        for num in nums:
            if num in ht:
                ht[num] += 1
            else:
                ht[num] = 1
            if ht[num] > maxOccur:
                maxOccur = ht[num]
        # put the num: freq into a prioroity queue
        for key in ht:
            heapq.heappush(pq, (maxOccur-ht[key], key))
        # pop the first k element from the priority queue
        res = []
        for i in range(k):
            pri, key = heapq.heappop(pq)
            res.append(key)

        return res


print(Solution().topKFrequent([], 0))
print(Solution().topKFrequent([], 1))
print(Solution().topKFrequent([1], 0))
print(Solution().topKFrequent([1], 1))
print(Solution().topKFrequent([1], 2))
print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(Solution().topKFrequent(
    [1, 1, 1, 2, 2, 3, 4, 1, 2, 1, 3, 3, 4, 3], 2))


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        2nd approach
        - count num: freq into a hashtable
        - use quick select the arrange the k-1 smallest elements present before kth elements

        48ms beats 34.16%
        21mar2019
        """
        if k > len(nums):
            return []
        # a list of tuples, for value it is (value, freq)
        counts = list(collections.Counter(nums).items())
        kth = self.kthBiggest(counts, k)
        res = []
        for x in counts[:kth+1]:
            res.append(x[0])
        return res

    def kthBiggest(self, nums, k):
        return self.helper(nums, 0, len(nums)-1, k)

    def helper(self, nums, left, right, k):
        if k > 0 and k <= len(nums):
            pIdx = self.partition(nums, left, right)
            if pIdx+1 == k:
                return pIdx
            elif pIdx+1 < k:
                return self.helper(nums, pIdx+1, right, k)
            else:
                return self.helper(nums, left, pIdx-1, k)
        return -1

    def partition(self, nums, left, right):
        pivot = nums[right][1]
        pIdx = left
        for i in range(left, right):
            # > for descending
            if nums[i][1] > pivot:
                nums[i], nums[pIdx] = nums[pIdx], nums[i]
                pIdx += 1
        nums[pIdx], nums[right] = nums[right], nums[pIdx]
        return pIdx


print(Solution().topKFrequent([1, 1, 1, 2, 2, 3, 4, 1, 2, 1, 3, 3, 4, 3], 2))
