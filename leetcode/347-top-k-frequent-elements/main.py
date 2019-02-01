import heapq


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
